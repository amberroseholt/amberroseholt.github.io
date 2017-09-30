import yaml
import os

YAML_FILE = "gallery.md"
FOLDERS = ["_tattoos","_brows","_commission"]

#Directory of this file
dir = os.path.dirname(__file__)

#For each gallery directory, find all files and build the yaml.
for folder in FOLDERS: 

	#generate the path to the yaml file Jekyll will use
    folderpath = os.path.join(dir, folder)
    yamlfile = os.path.join(folderpath, YAML_FILE)

    #Generate a list of images the yaml file knows about
    #These images won't need compressing as they already are.
    knownimages = []
    if os.path.exists(yamlfile):
        stream = open(yamlfile, 'r')
        data = yaml.load_all(stream)
        knownimages = data.next()['images'] or []
        stream.close()
    
    #Generate a list of images that are there right now
    realimages = []
    for file in os.listdir(folderpath):
        if file.endswith(".jpg") or file.endswith(".jpeg"):
            realimages.append(file)
        elif file.endswith(".png"):
            realimages.append(file)

    #Some images may have been removed since the yaml was last updated
    #Let's remove those entries 
    images = [img for img in knownimages if img in realimages]
    
    #Now get the images that need compressing and adding to the yaml
    newimages = [img for img in realimages if img not in knownimages]

    #Compress the image and remember it
    for image in newimages:
        #TODO: Compress Image
        images.append(image)

    #Write the new yaml
    with open(yamlfile, 'w+') as outfile:
    	outfile.write("---\n")
        yaml.dump({'images':images}, outfile, default_flow_style=False)
        outfile.write("---")
