from sympy.printing.conventions import split_super_sub

def test_super_sub():
    assert split_super_sub("beta_13_2") == ("beta", [], ["13","2"])
    assert split_super_sub("beta_132_20") == ("beta", [], ["132","20"])
    assert split_super_sub("beta_13") == ("beta", [], ["13"])
    assert split_super_sub("x_a_b") == ("x", [], ["a","b"])
    assert split_super_sub("x_1_2_3") == ("x", [], ["1","2","3"])
    assert split_super_sub("x_a_b1") == ("x", [], ["a","b1"])
    assert split_super_sub("x_a_1") == ("x", [], ["a","1"])
    assert split_super_sub("x_1_a") == ("x", [], ["1","a"])
    assert split_super_sub("x_1^aa") == ("x", ["aa"], ["1"])
    assert split_super_sub("x_1__aa") == ("x", ["aa"], ["1"])
    assert split_super_sub("x_11^a") == ("x", ["a"], ["11"])
    assert split_super_sub("x_11__a") == ("x", ["a"], ["11"])
    assert split_super_sub("x_a_b_c_d") == ("x", [], ["a","b","c","d"])
    assert split_super_sub("x_a_b^c^d") == ("x", ["c","d"], ["a","b"])
    assert split_super_sub("x_a_b__c__d") == ("x", ["c","d"], ["a","b"])
    assert split_super_sub("x_a^b_c^d") == ("x", ["b","d"], ["a","c"])
    assert split_super_sub("x_a__b_c__d") == ("x", ["b","d"], ["a","c"])
    assert split_super_sub("x^a^b_c_d") == ("x", ["a","b"], ["c","d"])
    assert split_super_sub("x__a__b_c_d") == ("x", ["a","b"], ["c","d"])
    assert split_super_sub("x^a^b^c^d") == ("x", ["a","b","c","d"], [])
    assert split_super_sub("x__a__b__c__d") == ("x", ["a","b","c","d"], [])
    assert split_super_sub("alpha_11") == ("alpha", [], ["11"])
    assert split_super_sub("alpha_11_11") == ("alpha", [], ["11","11"])
