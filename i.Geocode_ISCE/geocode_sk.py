# Embedded file name: geocode_sk.py
import argparse
from osgeo import gdal, ogr, osr

def cmdLineParse():
    """
    Command line parser.
    """
    parser = argparse.ArgumentParser(description='Geocode an image using GDAL')
    parser.add_argument('-i', '--input', dest='infile', type=str, required=True, help='Input file to be geocoded')
    parser.add_argument('-l', '--lat', dest='latFile', type=str, required=True, help='latitude file in radar coordinate')
    parser.add_argument('-L', '--lon', dest='lonFile', type=str, required=True, help='longitude file in radar coordinate')
    parser.add_argument('-o', '--output', dest='outfile', type=str, required=True, help='Output file name')
    parser.add_argument('-c', '--coord', dest='csys', type=str, required=False, help='Output Coordinate System EPSG')
    parser.add_argument('-s', '--spacing', dest='spacing', type=str, required=False, help='List with x,y spacing in meters or lon lat [x,y]')
    parser.add_argument('-m', '--method', dest='method', type=str, required=False, help='Interpolation method "near, bilinear, cubic, cubicspline, lanczos, average, mode, max, min, med, q1, q3"')
    return parser.parse_args()


def geocodeUsingGdalWarp(infile, latfile, lonfile, outfile, outsrs, spacing, method, insrs = 4326, fmt = 'GTiff', bounds = None):
    """
    Geocode a swath file using corresponding lat, lon files
    """
    sourcexmltmpl = '    <SimpleSource>\n      <SourceFilename>{0}</SourceFilename>\n      <SourceBand>{1}</SourceBand>\n    </SimpleSource>'
    driver = gdal.GetDriverByName('VRT')
    tempvrtname = 'geocode.vrt'
    inds = gdal.OpenShared(infile, gdal.GA_ReadOnly)
    tempds = driver.Create(tempvrtname, inds.RasterXSize, inds.RasterYSize, 0)
    for ii in range(inds.RasterCount):
        band = inds.GetRasterBand(1)
        tempds.AddBand(band.DataType)
        tempds.GetRasterBand(ii + 1).SetMetadata({'source_0': sourcexmltmpl.format(infile, ii + 1)}, 'vrt_sources')

    sref = osr.SpatialReference()
    sref.ImportFromEPSG(insrs)
    srswkt = sref.ExportToWkt()
    tempds.SetMetadata({'SRS': srswkt,
     'X_DATASET': lonfile,
     'X_BAND': '1',
     'Y_DATASET': latfile,
     'Y_BAND': '1',
     'PIXEL_OFFSET': '0',
     'LINE_OFFSET': '0',
     'PIXEL_STEP': '1',
     'LINE_STEP': '1'}, 'GEOLOCATION')
    band = None
    tempds = None
    inds = None
    if spacing is None:
        spacing = [None, None]
    if method is None:
        method = 'near'
    if outsrs is None:
        outsrs = 'EPSG:4326'
    spacing = spacing.split(',')
    warpOptions = gdal.WarpOptions(format=fmt, xRes=spacing[0], yRes=spacing[1], dstSRS=outsrs, outputBounds=bounds, resampleAlg=method, geoloc=True)
    gdal.Warp(outfile, tempvrtname, options=warpOptions)
    return


if __name__ == '__main__':
    inps = cmdLineParse()
    geocodeUsingGdalWarp(inps.infile, inps.latFile, inps.lonFile, inps.outfile, inps.csys, inps.spacing, inps.method)
