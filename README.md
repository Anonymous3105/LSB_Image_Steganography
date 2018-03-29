# LSB_Image_Steganography
Steganography is the art of hiding the fact that communication is tak-
ing place, by hiding information in other information. The main file formats
that are used for steganography are Text, images, audio, video, protocol. This
project is developed for hiding information in any image file. For hiding secret
information in images, there exists a large variety of steganography techniques
some are more complex than others and all of them have respective strong and
weak points.
In this project, one such algorithm will be studied and analyzed based
on its ability to hide information, the sustainability of information embedded
on compression of the images, effect of loss of information on transmission of
the image. The algorithm used in this project is the LSB Algorithm (with cer-
tain unique modifications) to understand how an image is affected on the use of
different position of the bit to inculcated in the algorithm. LSB (Least Signifi-
cant Bit) substitution is the process of adjusting the least significant bit pixels of
the carrier image. It is a simple approach for embedding message into the image.

Project Usage

python3 bit_stegs.py <path/to/input/image> <Text to Embedded> <bit_position_to_embed> 
