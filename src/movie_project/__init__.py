# package is split across src and test directories
# ensure the package can include resources in other directories
__import__('pkg_resources').declare_namespace(__name__)
