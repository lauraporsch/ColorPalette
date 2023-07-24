# ColorPalette
Website that allows Users to upload an image and get the dominant colors used in it as RGB code

I used Numpy to process the image data. I am well aware, that there are existing tools like the extcolors library or the colorthief module.
However I decided to go the long way to fully understand image processing with Numpy and the use of 3D arrays to represent image data.
Processing the data with np.unique(data, axis=0, return_counts=True) and only taking the highest count, leads to color palette with very similar colors, 
I used the scikitlearn KMeans-clustering method to group similar colors together.

# What I learned / used for the first time:
## HTML / CSS:
- Uploading an image file on a website with HTML-tags <form> and <input>
- Creating a dropdown menu for User Input with the help of HTML-tags <form> and <select>
- Using CSS inline-style to pass over variables from Python Code (RGB colors)
## Python
- Checking the image file for the right file format
- Using Werkzeug Utilities to create a secure filename before saving the image file
- Processing images with the Pillow library, including resizing an image
## Numpy
- Turning an image into numpy 3D-array and how they represent RGB image data
- Reshaping a numpy ndarray
- Finding unique values and their counts in a numpy 2D-array
- Turning numpy 2D-arrays into a list
- Grouping similar arrays using scikitlearn KMeans-clustering

Homepage
  ![image](https://github.com/lauraporsch/ColorPalette/assets/127047376/7dac00ea-e231-4bd4-939d-28181bedd874)

After inital upload of image file
![image](https://github.com/lauraporsch/ColorPalette/assets/127047376/b7f90a8e-9288-4187-bd48-85e9ee9e706e)

Example of extracting 6 colors from the image file
![image](https://github.com/lauraporsch/ColorPalette/assets/127047376/372ab1d5-0618-4e6b-9fe4-0f367f7efd15)

Example of extracting 4 and 10 colors from the same image file
![image](https://github.com/lauraporsch/ColorPalette/assets/127047376/309f5ce9-cc54-49d4-875f-050489d2cdb8)

![image](https://github.com/lauraporsch/ColorPalette/assets/127047376/fdfcc2fe-9a46-4c30-a0e1-f67d39afb29a)





  


