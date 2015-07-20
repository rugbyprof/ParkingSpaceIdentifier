<?php

$filename = $argv[1];

print_r(get_average_colour($filename,false));

/**
 * Get the average pixel colour from the given file using Image Magick
 * 
 * @param string $filename
 * @param bool $as_hex      Set to true, the function will return the 6 character HEX value of the colour.    
 *                          If false, an array will be returned with r, g, b components.
 */
function get_average_colour($filename, $as_hex_string = true) {
  try {
    // Read image file with Image Magick
    $image = new Imagick($filename);
    $image->setImageColorspace(2);
    // Scale down to 1x1 pixel to make Imagick do the average
    $image->scaleimage(1, 1);
    /** @var ImagickPixel $pixel */
    if(!$pixels = $image->getimagehistogram()) {
      return null;
    }
  } catch(ImagickException $e) {
    // Image Magick Error!
    return null;
  } catch(Exception $e) {
    // Unknown Error!
    return null;
  }

  $pixel = reset($pixels);
  $rgb = $pixel->getcolor();

  if($as_hex_string) {
    return sprintf('%02X%02X%02X', $rgb['r'], $rgb['g'], $rgb['b']);
  }

   return $rgb;
}
