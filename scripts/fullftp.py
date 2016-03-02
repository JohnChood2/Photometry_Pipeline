#! /usr/bin/python
from astropy.io import fits 
make a file of all the fits file names
read the file and put to dummyfile
then loop through all the elements in dummyfile


do i=10,99
num=140531
num2=i
dummyfile=rccdnum.00num2.fits
hdulist = fits.open('rccdnum.00num2.fits')
hdulist[0].header['OBJECT']
hdulist[0].header['FILTER']
hdulist[0].header['FILENAME']

obj=hdulist[0].header['OBJECT']
filt=hdulist[0].header['FILTER']
fi=hdulist[0].header['FILENAME']

hdulist=file.close()

enddo





