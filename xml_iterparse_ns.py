#!/usr/bin/env python
from lxml.etree import iterparse

XML_FILE = '../DATA/libreoffice_content.xml'


TAG_LIST = [  # <1>
    'style:font-face',
    'text:list-style',
]


def main():
    nsmap = get_nsmap()  # <2>

    tag_list = [replace_prefix(tag, nsmap) for tag in TAG_LIST]  # <3>

    context = iterparse(XML_FILE, tag=tag_list)  # <4>

    for i, (event, element) in enumerate(context, 1):  # <5>
        print(element.tag)
        # <6>

        element.clear()  # <7>

        while element.getprevious() is not None:  # <8>
            del element.getparent()[0]

    print("found {} elements".format(i))


def get_nsmap():
    """
    Parse the entire file to get the embedded namespaces,
    an turn them into a dictionary for later use.

    Note -- you could write this to run separately, saving the nsmap in a file
    (pickle would work great here) and then reuse it for
    subsequent searches, rather than always having to parse twice.

    :return: Dict of namespace mappings
    """
    context = iterparse(XML_FILE, events=('start-ns',))  # <9>
    nsmap = dict(element for event, element in context)  # <10>
    return nsmap  # <11>


def replace_prefix(nstag, nsmap):
    """
    Replace the tag prefix with the actual namespace, surrounded by "{}", because
    this is what etree.iterparse() needs.

    :param nstag: A tag in the form:  "prefix:tag"
    :param nsmap: The dictionary of namespace mappings
    :return: A string with the full namespace as used by etree: "{namespace}tag"
    """
    prefix, tag = nstag.split(':', 1)  # split "prefix:tag" into both parts
    map = nsmap.get(prefix, "ERROR")   # get the namespace for that prefix
    return "{{{}}}{}".format(map, tag)  # return the namespace and tag in etree format

if __name__ == '__main__':
    main()
