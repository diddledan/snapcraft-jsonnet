==========
sc-jsonnet
==========

This is the documentation of **sc-jsonnet**.

Howto
=====

First you need to get **sc-jsonnet** from the snap store:

.. code-block:: bash

    sudo snap install sc-jsonnet

Now you have the program you need to make a file called
`snapcraft.jsonnet` in your snapcraft project at
`./snap/local/snapcraft.jsonnet`. Add the following to begin with:

.. code-block::
    :caption: snap/local/snapcraft.jsonnet

    local snapcraft = import 'snapcraft.libsonnet';

    snapcraft {
        name: "my-jsonnet-snap-name",
        version: "0.1",
        summary: "Single-line elevator pitch for your amazing snap",
        description: "This is my-snap's description. You have a paragraph or two to tell the most important story about your snap. Keep it under 100 words though, we live in tweetspace and your description wants to look good in the snap store.",
        grade: "devel",
        confinement: "devmode",

        parts: {
            "my-part": {
                plugin: "nil",
            },
        },
    }

Finally we need to run the translation step to convert the jsonnet
into yaml for `snapcraft` to use. First, we run `sc-jsonnet`
without any parameters to see the yaml that will be produced:

.. code-block:: bash

    sc-jsonnet

Now we have verified that everything works, we can run with
`-o snap/snapcraft.yaml` to save into your project `snapcraft.yaml`
for the snapcraft tool to use:

.. code-block:: bash

    sc-jsonnet -o snap/snapcraft.yaml


Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _toctree: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _reStructuredText: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _references: http://www.sphinx-doc.org/en/stable/markup/inline.html
.. _Python domain syntax: http://sphinx-doc.org/domains.html#the-python-domain
.. _Sphinx: http://www.sphinx-doc.org/
.. _Python: http://docs.python.org/
.. _Numpy: http://docs.scipy.org/doc/numpy
.. _SciPy: http://docs.scipy.org/doc/scipy/reference/
.. _matplotlib: https://matplotlib.org/contents.html#
.. _Pandas: http://pandas.pydata.org/pandas-docs/stable
.. _Scikit-Learn: http://scikit-learn.org/stable
.. _autodoc: http://www.sphinx-doc.org/en/stable/ext/autodoc.html
.. _Google style: https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings
.. _NumPy style: https://numpydoc.readthedocs.io/en/latest/format.html
.. _classical style: http://www.sphinx-doc.org/en/stable/domains.html#info-field-lists
