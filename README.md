
This repository is a [DataLad] dataset generated from [Retrosheet's
game logs][rgl].

The directory was populated using `datalad crawl`, which was
configured to download the game log zip files as well as a few
metadata files (see [.datalad/crawl/crawl.cfg][cfg]).  The branch
`incoming` contains the original zip files, whereas the branch
`master` has the extracted text files.  To fetch the latest game logs
from the Retrosheet site, call `datalad crawl`.

[DataLad]: http://datalad.org/
[rgl]: http://www.retrosheet.org/gamelogs/
[cfg]: https://github.com/kyleam/retrosheet-gamelogs/tree/master/.datalad/crawl/crawl.cfg
