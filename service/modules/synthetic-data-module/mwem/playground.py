#%%
import numpy as np
n = np.array([[[1., 2., 3.],
        [4., 5., 6.],
        [7., 8., 9.]],
        [[10., 11., 12.],
        [13., 14., 15.],
        [16., 17., 18.]],
        [[19., 20., 21.],
        [22., 23., 24.],
        [25., 26., 27.]]])

# n = np.array(
#     [[1., 2., 3.],
#     [4., 5., 6.],
#     [7., 8., 9.]])

dims = np.array(n.shape)
inds = []
for i,s in np.ndenumerate(np.array(n.shape)):
    print(s)
    a = np.random.randint(s)
    b = np.random.randint(s)

    l_b = min(a,b) ; u_b = max(a,b) + 1
    pre = []
    pre.append(l_b)
    pre.append(u_b)
    inds.append(pre)

print(inds)
spots = np.ravel_multi_index(inds, n.shape, mode='clip')
n_view = np.ravel(n)
print(n_view[spots[0]])
print(n_view[spots[1]])
print(spots)
n.T[inds[0][0]:inds[0][1],inds[1][0]:inds[1][1]].T

# sl = []
# for i in dims:
#     for j in dims[i]:
#         sl.append[]
# print(n[spots_1][spots_2])
# np.ravel(n)[spots_1[0]:spots_2[0]]
# np.ravel(n)[spots_1[1]:spots_2[1]]


#%%
slices_list = []
# TODO: For analysis, generate a distribution of slice sizes,
# by running the list of slices on a dimensional array
# and plotting the bucket size
for _ in range(1):
    # Random linear sample, within dimensions
    # i.e. a contiguous query for the flattened dims
    len_ind = np.prod(dimensions)
    a = np.random.randint(len_ind)
    b = np.random.randint(len_ind)
    while a == b:
        a = np.random.randint(len_ind)
        b = np.random.randint(len_ind)
    # Set bounds and add the slice
    l_b = min(a,b) ; u_b = max(a,b)
    slices_list.append(np.s_[l_b:u_b])
