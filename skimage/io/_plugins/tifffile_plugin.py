from warnings import warn

from tifffile import TiffFile, imsave, parse_kwargs


def imread(fname, dtype=None, **kwargs):
    """Load a tiff image from file.

    Parameters
    ----------
    fname : str or file
       File name or file-like-object.
    dtype : numpy dtype object or string specifier
       Specifies data type of array elements.
       Will be removed from version 0.17.
    kwargs : keyword pairs, optional
        Additional keyword arguments to pass through (see ``tifffile``'s
        ``imread`` function).

    Notes
    -----
    Provided by Christophe Golhke's tifffile.py [1]_, and supports many
    advanced image types including multi-page and floating point.

    References
    ----------
    .. [1] http://www.lfd.uci.edu/~gohlke/code/tifffile.py

    """
    if dtype is not None:
        warn('The dtype argument was always silently ignored. It will be '
             'removed from scikit-image version 0.17. To avoid this '
             'warning, do not specify it in your function call.',
             UserWarning, stacklevel=2)

    if 'img_num' in kwargs:
        kwargs['key'] = kwargs.pop('img_num')

    # parse_kwargs will extract keyword arguments intended for the TiffFile
    # class and remove them from the kwargs dictionary in-place
    tiff_keys = ['multifile', 'multifile_close', 'fastij', 'is_ome']
    kwargs_tiff = parse_kwargs(kwargs, *tiff_keys)

    # read and return tiff as numpy array
    with TiffFile(fname, **kwargs_tiff) as tif:
        return tif.asarray(**kwargs)
