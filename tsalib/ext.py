from tsalib.ts import TS


def view_transform (src, to, in_shape):
    '''
    View Transform
    :src is the source view, each element is a single named dim variable
    :to is the target view, may contain expressions over named dim variables
    :in_shape is the shape of the source tensor
    :returns the new size of the tensor after view transformation
    '''
    assert isinstance(src, (list, tuple))
    assert isinstance(to, (list, tuple))
    assert isinstance(in_shape, (list, tuple))

    #sub_map = [(d.e, Symbol(f'{i}')) for i, d in enumerate(src)]
    sub_map = [(d.e, in_shape[i]) for i, d in enumerate(src)]
    out_shape = tuple([t.e.subs(sub_map) if isinstance(t, TS) else t for t in to])

    return out_shape

def permute_transform(src, to):
    '''
    Permute Transform
    :src is the source dimension arrangement, each element is a single named dim variable
    :to is the target dimension arragement, each element is a single named dim variable
    :returns the index tuple for the permutation
    '''
    assert isinstance(src, (list, tuple))
    assert isinstance(to, (list, tuple))
    sub_map = [(d.e, i) for i, d in enumerate(src)]
    perm_indices = tuple([t.e.subs(sub_map) for t in to])
    return perm_indices






