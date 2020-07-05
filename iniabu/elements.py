"""Element handler.

This class manages the elements. It must be called from :class:`iniabu.IniAbu`.
"""


import numpy as np

from .utilities import return_value_simplifier


class Elements(object):
    """Class representing the elements.

    This is mainly a list to easily interact with the `parent._ele_dict` dictionary.

    Example:
        >>> from iniabu import ini
        >>> element = ini.element["Si"]
        >>> element.solar_abundance
        999700.0

    .. warning:: This class should NOT be manually created by the user. It is
        designed to be initialized by :class:`iniabu.IniAbu`.
    """

    def __init__(self, parent, eles):
        """Initialize the Elements class.

        Checks for initialization from the proper parent class and sets up the required
        dictionaries to be used later.

        :param parent: Parent class.
        :type parent: class:`iniabu.IniAbu`
        :param eles: Element dictionary.
        :type eles: dict

        :raises TypeError: The class was not initialized with :class:`iniabu.IniAbu`
            as the parent.
        """
        # check for correct parent
        if parent.__class__.__name__ != "IniAbu":
            raise TypeError("Elements class must be initialized from IniAbu.")

        # set the variables
        self._eles = eles
        self._ele_dict = parent.ele_dict

    # PROPERTIES #

    @property
    def isotopes_a(self):
        """Get the atomic number(s) of all isotopes.

        Returns the atomic number(s) of all isotopes of this element as a numpy integer
        ndarray. If more than one element is selected, a list of numpy integer arrays
        is returned.

        :return: Atomic numbers of all isotopes
        :rtype: ndarray,list<ndarray>
        """
        ret_arr = []
        for ele in self._eles:
            ret_arr.append(np.array(self._ele_dict[ele][1], dtype=np.int))
        return return_value_simplifier(ret_arr)

    @property
    def isotopes_relative_abundance(self):
        """Get relative abundance of all isotopes.

        Returns a list with the relative abundances of all isotopes of the given
        element. If more than one element is selected, a list of numpy float ndarrays is
        returned. Note: All relative abundances sum up up to unity.

        :return: Relative abundance of all isotopes
        :rtype: ndarray,list<ndarray>
        """
        ret_arr = []
        for ele in self._eles:
            ret_arr.append(np.array(self._ele_dict[ele][2], dtype=np.float))
        return return_value_simplifier(ret_arr)

    @property
    def isotopes_solar_abundance(self):
        """Get solar abundances of all isotopes.

        Returns a list with the solar abundances of all isotopes of the given element.
        If more than one element is selected, a list of numpy float ndarrays is
        returned. Note: Not all databases contain this information. If the information
        is not available, these values will be filled with ``np.nan``.

        :return: Relative abundance of all isotopes
        :rtype: ndarray,list<ndarray>
        """
        ret_arr = []
        for ele in self._eles:
            ret_arr.append(np.array(self._ele_dict[ele][3], dtype=np.float))
        return return_value_simplifier(ret_arr)

    @property
    def solar_abundance(self):
        """Get solar abundance of element(s).

        Returns the solar abundance of the selected element(s). Returns the result
        either as a ``float`` or as a numpy ``ndarray``. Note: Not all databases contain
        this information. If the information is not available, these values will be
        filled with ``np.nan``.

        :return: Solar abundance of element(s)
        :rtype: float,ndarray
        """
        ret_arr = []
        for ele in self._eles:
            ret_arr.append(self._ele_dict[ele][0])
        ret_arr = np.array(ret_arr)
        return return_value_simplifier(ret_arr)