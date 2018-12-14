"""Pipeline for Retrosheet game logs.
"""

from datalad_crawler.nodes.crawl_url import crawl_url
from datalad_crawler.nodes.matches import a_href_match
import datalad_crawler.pipelines.simple_with_archives as sa


def pipeline():
    incoming = [
        [
            crawl_url("http://www.retrosheet.org/parkcode.txt"),

        ],
        [
            crawl_url("http://www.retrosheet.org/retroID.htm"),
        ],
        crawl_url("http://www.retrosheet.org/gamelogs/"),
        a_href_match(".*/(glfields\.txt|gl....\.zip)",
                     min_count=1),
    ]

    return sa.pipeline(incoming_pipeline=incoming,
                       add_annex_to_incoming_pipeline=True)
