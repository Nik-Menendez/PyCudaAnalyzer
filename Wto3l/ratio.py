import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.axes as ax

def centers_of_binning_array(bin_arr, decimals=0):
    """
    Returns an array of the centers between adjacent bin edges.
    Also works with bin_arr that has unequal bin widths. 
    
    Example: 
        bin_arr = np.array([1, 2, 4, 8])
        returns: np.array([1.5, 3, 6])
        
    NOTE: Was formerly called shift_binning_array().
    
    Parameters
    ----------
    bin_arr : list or array-like
        Edges of bins: [left_edge_first_bin, ..., right_edge_last_bin]
    decimals : int, optional
        Number of decimal places to round bin centers.
        
    Returns
    -------
    bin_centers_arr : array
        Centers between adjacent bin edges.
        Will be of length = len(bin_arr) - 1
    """
    bin_arr = np.array(bin_arr)
    bin_edges_low = bin_arr[:-1]
    bin_edges_high = bin_arr[1:]
    
    bin_centers_arr = (bin_edges_high + bin_edges_low) / 2.
    if decimals != 0:
        bin_centers_arr = np.round(bin_centers_arr, decimals=decimals)
    
    return bin_centers_arr

def calc_x_err_bins_from_bin_edges(bin_edge_ls, bin_center_ls=None):
    """
    Returns lists of the "x-errors", i.e. the half-distances between neighboring bins.
    These may be symmetrical or asymmetrical.
    Example:
    bin_edge_ls = [0, 2, 5, 10]
    bin_center_ls = [1, 4, 8]
    returns: (
        [1, 2, 3],
        [1, 1, 2]
        )
    Parameters
    ----------
    bin_edge_ls : list or array-like
        The edges of the bins along the x-axis.
        len(bin_edge_ls) should equal len(n_bins) + 1.
    bin_center_ls : list or array-like, optional
        len(bin_center_ls) shoudl equal len(n_bins).
    Returns
    -------
    2-tuple : (low_err_arr, high_err_arr)
    - low_err_arr is the array of x-err bars on the left side of each point.
    - high_err_arr is the array of x-err bars on the right side of each point.
    """
    bin_arr = np.array(bin_edge_ls)
    bin_edges_low = bin_arr[:-1]
    bin_edges_high = bin_arr[1:]

    if bin_center_ls is None:
        bin_center_ls = centers_of_binning_array(bin_arr)

    assert len(bin_center_ls) + 1 == len(bin_edge_ls)

    low_err_arr = bin_center_ls - bin_edges_low
    high_err_arr = bin_edges_high - bin_center_ls
    
    return (low_err_arr, high_err_arr)

def prop_err_x_div_y(x, y, dx, dy):
    """
    Return the ratio of two numbers (r = x/y) and the 
    corresponding uncertainty (dr), depending on (x, y, dx, dy).
    The error propagation formula is:
        (dr)^2 = (dr/dx)^2 * (dx)^2 + (dr/dy)^2 * (dy)^2 + 2*dr/dx*dr/dy * dx*dy
        but we will ignore the final cross-term (correlation factor).
            Newton says: 
            dr/dx = 1/y
            dr/dy = -x/(y^2)
        So:
            dr = sqrt( (dx/y)^2 + (-x/(y)^2 * dy)^2 )
    *** This function been verified by an online calculator.
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    dx = np.array(dx, dtype=float)
    dy = np.array(dy, dtype=float)
    
    undef = np.ones_like(x) * np.inf
    # Where denom is not 0, do the division. Elsewhere put inf.
    r = np.true_divide(x, y, out=undef, where=y!=0)
    # r = x / y
    dr = np.sqrt((dx / y)**2 + (x / y**2 * dy)**2)
    return r, dr

# Error bar variables
al=1  # alpha=0 is transparent
elw=2  # error bar line width
ecolor='k'
ms=12  # marker size
mec='k'  # marker edge color
cs=4  # cap size
mew=1  # marker edge width

#----------Tighter Iso----------------------
#ePD_b = np.array([57223, 9450, 1626, 1085, 1151])
#ePW_b = np.array([113, 280, 325, 429, 580])
#eFD_b = np.array([62063, 26158, 7573, 3820, 1804])
#eFW_b = np.array([48, 33, 16, 8, 6])
#
#ePD_e = np.array([42285, 6008, 1016, 614, 628])
#ePW_e = np.array([73, 155, 193, 249, 303])
#eFD_e = np.array([28854, 9749, 2317, 1030, 416])
#eFW_e = np.array([24, 13, 6, 3, 2])
#--------------------------------

#----------More Bins----------------------
#ePD_b = np.array([57223, 9450, 1626, 1085, 574, 403, 174])
#ePW_b = np.array([113, 280, 325, 429, 280, 200, 100])
#eFD_b = np.array([62063, 26158, 7573, 3820, 1173, 494, 137])
#eFW_b = np.array([48, 33, 16, 8, 4, 2, 1])
#
#ePD_e = np.array([42285, 6008, 1016, 614, 311, 223, 94])
#ePW_e = np.array([73, 155, 193, 249, 155, 100, 48])
#eFD_e = np.array([28854, 9749, 2317, 1030, 270, 114, 32])
#eFW_e = np.array([24, 13, 6, 3, 1, 1, 0])
#--------------------------------

#----------JPsi Veto----------------------
ePD_b = np.array([54024, 8880, 1549, 1055, 567, 397, 172])
ePW_b = np.array([106, 272, 318, 425, 277, 199, 99])
eFD_b = np.array([59033, 25421, 7473, 3798, 1171, 494, 137])
eFW_b = np.array([46, 32, 16, 8, 4, 2, 1])

ePD_e = np.array([40783, 5744, 967, 594, 304, 217, 94])
ePW_e = np.array([70, 150, 190, 247, 154, 99, 48])
eFD_e = np.array([27634, 9493, 2288, 1021, 270, 114, 32])
eFW_e = np.array([23, 13, 6, 3, 1, 1, 0])
#--------------------------------

#pT = np.array([7.5,15,25,37.5,62.5])
#binny = np.array([5,10,20,30,45,100])

pT = np.array([7.5,15,25,37.5,52.5,70,90])
binny = np.array([5,10,20,30,45,60,80,100])

ratio_b = np.divide((ePD_b-ePW_b),(eFD_b-eFW_b)+(ePD_b-ePW_b))
ratio_e = np.divide((ePD_e-ePW_e),(eFD_e-eFW_e)+(ePD_e-ePW_e))

ratio_b, err_b = prop_err_x_div_y((ePD_b-ePW_b),(eFD_b-eFW_b)+(ePD_b-ePW_b),0,0)
ratio_e, err_e = prop_err_x_div_y((ePD_e-ePW_e),(eFD_e-eFW_e)+(ePD_e-ePW_e),0,0)

low_x_err, high_x_err = calc_x_err_bins_from_bin_edges(binny)

print("Barrel:")
print(ratio_b)
print("Endcap:")
print(ratio_e)

#plt.title("Events Passing Iso and TightId Cuts/Events Failing for 2e+1mu Events")
plt.title("Muon Fake Rate")
plt.xlabel("Muon pT")
plt.ylabel("Passed/Total")
plt.xlim([5,100])

barrel = plt.plot(pT,ratio_b,'_b',markersize=20, label='Barrel')
endcap = plt.plot(pT,ratio_e,'_r',markersize=20, label='Endcap')

barrel = plt.errorbar(pT, ratio_b, xerr=[low_x_err, high_x_err], yerr=err_b, fmt='o',label='Barrel', color='b', elinewidth=elw, ms=ms, markeredgecolor=mec, capsize=cs, mew=mew, ecolor=ecolor)
endcap = plt.errorbar(pT, ratio_e, xerr=[low_x_err, high_x_err], yerr=err_e, fmt='o',label='Endcap', color='r', elinewidth=elw, ms=ms, markeredgecolor=mec, capsize=cs, mew=mew, ecolor=ecolor)

blue_patch = mpatches.Patch(color='blue', label='Barrel')
red_patch = mpatches.Patch(color='red', label='Endcap')

plt.legend(handles=[blue_patch,red_patch], loc='upper right')

plt.savefig('output/2017_Data_Driven_Background/FakeRate.png')
plt.show()
