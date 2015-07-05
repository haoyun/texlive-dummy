Dummy Package of TeXlive For Fedora
===================================

This is the source of a dummy package of TeXLive for Fedora.
To get the rpm package, simply run, for example

    rpmbuild -bb texlive-dummy.spec

I noticed that some packages require programs as dependency using absolute path, e.g., `/usr/bin/mktexlsr`, `/usr/bin/fmtutil` and `/usr/bin/texhash`, which are included in the TeXlive DVD distribution. So I also add them to the list except the usual `texlive-*` ones. 
