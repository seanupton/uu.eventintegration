
def initialize(context):
    """Make this package a zope2 product"""
    import patch
    # apply monkey patches
    patch.patch_widget()
    patch.patch_ulocalized_time()

