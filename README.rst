==========
sc-jsonnet
==========


Build your snapcraft.yaml with jsonnet!


Description
===========

Use jsonnet syntax to build your snapcraft.yaml.

For information about jsonnet see https://jsonnet.org/


Howto
=====

First you need to get **sc-jsonnet** from the snap store. Either run:

.. code-block:: bash

    sudo snap install sc-jsonnet

Or click the following button to go to the store where you can install it using
the GUI:

.. image:: https://snapcraft.io/static/images/badges/en/snap-store-black.svg
    :alt: Get it from the Snap Store
    :target: https://snapcraft.io/sc-jsonnet

Now you have the program you need to make a file called
``snapcraft.jsonnet`` in your snapcraft project at
``./snap/local/snapcraft.jsonnet``. Add the following to begin with::

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
into yaml for ``snapcraft`` to use. First, we run ``sc-jsonnet``
without any parameters to see the yaml that will be produced:

.. code-block:: bash

    sc-jsonnet

Now we have verified that everything works, we can run with
``-o snap/snapcraft.yaml`` to save into your project
``snapcraft.yaml`` for the snapcraft tool to use:

.. code-block:: bash

    sc-jsonnet -o snap/snapcraft.yaml


Note
====

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
