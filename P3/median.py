import nose.tools as nt

#def median(data):
#    """Returns the median of a dataset."""
#    data.sort()
#    return data[len(data)//2]

def median(data):
    """Returns the median of a dataset."""
    if data == [] or data == ():
        raise ValueError("List or tuple must contain at least 1 element")
    data = data.copy()
    data.sort()
    if len(data)%2 == 0:
        return (data[len(data)//2] + data[len(data)//2 - 1])/2
    else:
        return data[len(data)//2]

def test_median():
    data1 = [11, 3, 1, 5, 3];
    data2 = [3,2];
    data3 = [2];
    data4 = [1, 2, 3, 4, 5, 6, 7];
    data4backup = data4.copy()

    nt.assert_equal(median(data1), 3);
    nt.assert_equal(median(data2), 2.5);
    nt.assert_equal(median(data3), 2);
    nt.assert_equal(median(data4), 4);

    median(data4)
    nt.assert_equal(data4backup, data4);

@nt.raises(ValueError)
def test_median_value1():
    median([])

@nt.raises(ValueError)
def test_median_value2():
    median(())
