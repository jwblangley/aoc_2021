from day12 import Cave, count_paths_to_end


def test_count_paths_to_end_basic():
    # GIVEN
    start = Cave("start")
    end = Cave("end")

    start.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 1


def test_count_paths_to_end_single_path():
    # GIVEN
    start = Cave("start")
    a = Cave("a")
    end = Cave("end")

    start.connect(a)
    a.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 1


def test_count_paths_to_end_single_path_big_cave():
    # GIVEN
    start = Cave("start")
    a = Cave("A")
    end = Cave("end")

    start.connect(a)
    a.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 1


def test_count_paths_to_end_one_split():
    # GIVEN
    start = Cave("start")
    a = Cave("a")
    b = Cave("b")
    end = Cave("end")

    start.connect(a)
    start.connect(b)
    a.connect(end)
    b.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 2


def test_count_paths_to_end_one_split_that_merges():
    # GIVEN
    start = Cave("start")
    a = Cave("a")
    aa = Cave("aa")
    b = Cave("b")
    bb = Cave("bb")
    end = Cave("end")

    start.connect(a)
    start.connect(b)

    a.connect(aa)
    b.connect(bb)

    aa.connect(end)
    bb.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 2


def test_count_paths_to_end_larger():
    # GIVEN
    start = Cave("start")
    end = Cave("end")
    a = Cave("A")
    b = Cave("b")
    c = Cave("c")
    d = Cave("d")

    start.connect(a)
    start.connect(b)
    a.connect(c)
    a.connect(b)
    b.connect(d)
    a.connect(end)
    b.connect(end)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 10


def test_count_paths_to_end_complex():
    # GIVEN
    start = Cave("start")
    end = Cave("end")
    dc = Cave("dc")
    hn = Cave("HN")
    kj = Cave("kj")
    ln = Cave("LN")
    sa = Cave("sa")

    dc.connect(end)
    hn.connect(start)
    start.connect(kj)
    dc.connect(start)
    dc.connect(hn)
    ln.connect(dc)
    hn.connect(end)
    kj.connect(sa)
    kj.connect(hn)
    kj.connect(dc)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 19


def test_count_paths_to_end_very_complex():
    # GIVEN
    start = Cave("start")
    end = Cave("end")
    fs = Cave("fs")
    he = Cave("he")
    dx = Cave("DX")
    pj = Cave("pj")
    zg = Cave("zg")
    sl = Cave("sl")
    rw = Cave("RW")
    wi = Cave("WI")

    fs.connect(end)
    he.connect(dx)
    fs.connect(he)
    start.connect(dx)
    pj.connect(dx)
    end.connect(zg)
    zg.connect(sl)
    zg.connect(pj)
    pj.connect(he)
    rw.connect(he)
    fs.connect(dx)
    pj.connect(rw)
    zg.connect(rw)
    start.connect(pj)
    he.connect(wi)
    zg.connect(he)
    pj.connect(fs)
    start.connect(rw)

    # WHEN
    res = count_paths_to_end(start)

    # THEN
    assert res == 226
