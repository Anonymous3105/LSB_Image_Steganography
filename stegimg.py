from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="image_enc.png", bit_to_decode=-1):
	encoded_image = Image.open(file_location)
	red_channel = encoded_image.split()[0]

	x_size = encoded_image.size[0]
	y_size = encoded_image.size[1]

	decoded_image = Image.new("RGB", encoded_image.size)
	pixels = decoded_image.load()

	for i in range(x_size):
		for j in range(y_size):
			if format(red_channel.getpixel((i, j)), '#010b')[2:][bit_to_decode] == '0':
				pixels[i, j] = (255, 255, 255)
			else:
				pixels[i, j] = (0,0,0)

	new_img_name = file_location.split("_enc")[0] + "_text.png"
	decoded_image.save(new_img_name)
	return new_img_name

def write_text(text_to_write, image_size):
	image_text = Image.new("RGB", image_size)
	font = ImageFont.load_default().font
	drawer = ImageDraw.Draw(image_text)

	margin = offset = 10

	for line in textwrap.wrap(text_to_write, width=60):
		drawer.text((margin,offset), line, font=font)
		offset += 10
	return image_text

def encode_image(text_to_encode, template_image_name="image.jpg", bit_to_encode=-1):
	template_image = Image.open(template_image_name)
	red_template = template_image.split()[0]
	green_template = template_image.split()[1]
	blue_template = template_image.split()[2]

	x_size = template_image.size[0]
	y_size = template_image.size[1]

	image_text = write_text(text_to_encode, template_image.size)
	bw_encode = image_text.convert('1')

	encoded_image = Image.new("RGB", (x_size, y_size))
	pixels = encoded_image.load()
	for i in range(x_size):
		for j in range(y_size):
			red_template_pix = format(red_template.getpixel((i,j)), '#010b')[2:]
			old_pix = red_template.getpixel((i,j))
			tencode_pix = bin(bw_encode.getpixel((i,j)))

			if tencode_pix[-1] == '1':
				# red_template_pix = '1' + red_template_pix[1:]
				temp = list(red_template_pix)
				temp[bit_to_encode] = '1'
				red_template_pix = "".join(temp) 
			else:
				# red_template_pix = '0' + red_template_pix[:-1]
				temp = list(red_template_pix)
				temp[bit_to_encode] = '0'
				red_template_pix = "".join(temp) 
			pixels[i, j] = (int(red_template_pix, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))
	new_img_name = template_image_name.split('.')[0] + "_enc.png"
	encoded_image.save(new_img_name)
	return new_img_name