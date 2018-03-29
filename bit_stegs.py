from stegimg import decode_image, write_text, encode_image
import sys

if len(sys.argv) > 1:
	input_image = sys.argv[1]
	bit_to_use = int(sys.argv[2])
	# text_to_encode = str(sys.argv)[2]
else:
	input_image = "image.jpg"
	bit_to_use = -1	
	# text_to_encode = "Hello world"
# input_image = "image.jpg"
# bit_to_use = 3	


text_to_encode = "Lorem ipsum officia dolore duis adipisicing labore mollit id elit officia elit consectetur voluptate cupidatat ea magna do anim enim commodo labore officia nostrud pariatur quis nostrud sed velit nisi aliquip nostrud in veniam consequat amet pariatur ad id labore do ut deserunt dolor in ullamco excepteur pariatur elit in exercitation nostrud culpa officia labore excepteur velit aliqua aliquip sit culpa ex non enim esse aute mollit aliqua exercitation voluptate magna est ea dolore aliquip exercitation exercitation sunt ea enim proident dolor esse proident nisi in excepteur pariatur do ut nulla officia ut do elit aliquip excepteur sint aliqua pariatur qui non duis excepteur commodo minim id eu occaecat qui labore est minim ut exercitation mollit pariatur commodo esse dolore voluptate ut ex aliquip dolor tempor dolore cillum nulla et cillum ea magna sed aliqua sed eu quis magna labore occaecat duis ad exercitation ut elit quis cillum in tempor sed sunt in laborum tempor in ea eu dolore esse nulla minim mollit sit ad adipisicing irure labore laborum nisi ullamco reprehenderit ea dolor sunt in consequat velit in commodo magna non commodo veniam quis do ea exercitation laboris ut ea amet elit eiusmod ut anim pariatur commodo id qui amet est veniam culpa incididunt id laborum sed qui sunt proident quis amet sit proident dolore commodo nisi enim mollit est officia aute laboris ut cupidatat in voluptate magna deserunt dolore sunt dolore quis elit in cillum."
# text_to_encode = "Ullamco cillum deserunt"

encoded_image = encode_image(text_to_encode, input_image, bit_to_use)
decoded_image = decode_image(encoded_image, bit_to_use)