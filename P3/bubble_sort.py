import nose.tools as nt

def sort(List):
    """
    Copies the list or tuple given, and returns a list sorted
    with the boubble-sort regime
    """
    if not isinstance(List, (list, tuple)):
        raise TypeError("Argument must be list or tuple")
    List = list(List).copy()
    sorted = False
    iter = len(List) - 1
    while (sorted == False):
        sorted = True
        for i in range(iter):
            if List[i] > List[i+1]:
                List[i],List[i+1] = List[i+1],List[i]
                sorted = False
        iter -= 1

    return List

def test_sort():
    list1 = [];             list1sorted = []
    list2 = [1];            list2sorted = [1]
    list3 = [1,2,3,4];      list3sorted = [1,2,3,4]
    list4 = [4,1,2,3,7,5,0];list4sorted = [0,1,2,3,4,5,7]
    list5 = (4,1,2,3,7,5,0);list5sorted = (0,1,2,3,4,5,7)
    list6 = [6,6,3,3,6];    list6sorted = [3,3,6,6,6]

    list6backup = list6.copy()

    nt.assert_equal(sort(list1),list1sorted)
    nt.assert_equal(sort(list2),list2sorted)
    nt.assert_equal(sort(list3),list3sorted)
    nt.assert_equal(sort(list4),list4sorted)
    nt.assert_equal(sort(list5),list(list5sorted))

    sort(list6)
    nt.assert_equal(list6,list6backup)

@nt.raises(TypeError)
def test_sort_value1():
    sort("1,2,3,4")

@nt.raises(TypeError)
def test_sort_value2():
    sort(1)
