import PIL
from PIL import Image

def main():
	image_name = input("Which image would you like to resize? (add file extension): ")
	new_name = input("What would you like to name the new image? (add file extension): ").lower()
	format_it = formatter(new_name)
	image_size = image_dimensions(image_name)
	image_resize(image_name, image_size, new_name, format_it)
	
def image_dimensions(image_name):
	print('''Resizing Method:
	1. Percentage
	2. Custom dimensions''')
	image_factor = input("How would you like to resize the image?: ")
	image = Image.open(f"source/{image_name}")
	height, width = image.size
	if "custom" in image_factor.lower():
		height = float(input("What is the height of the image?: "))
		width = float(input("What is the width of the image?: "))
		return ({"height": height, "width": width})
	elif "percent" in image_factor.lower():
		percentage = float(input("What percentage do you want to shrink the image by?(enter in decimals i.e. 0.5 = 50%): "))
		return ({"height":round(height*percentage), "width": round(width*percentage)})

def formatter(new_name):
	if "jpg" in new_name:
		return "jpg"
	elif "png" in new_name:
		return "png"
	elif "ico" in new_name:
		return "ico"
		
def image_resize(image_name, image_factor, new_name, format_it):
	image = Image.open(f"source/{image_name}")
	resized_image = image.resize((round(image_factor.get("width")), round(image_factor.get("height"))))
	resized_image.show()
	keep_going = input("Would you like to save the resized image?: ")
	if "yes" in keep_going.lower():
		resized_image.save(f"generated/{new_name}", format=format_it)
	elif "no" in keep_going.lower():
		exit()
	else:
		resized_image.save(f"generated/{new_name}", format=format_it)

if __name__=="__main__":
	main()
