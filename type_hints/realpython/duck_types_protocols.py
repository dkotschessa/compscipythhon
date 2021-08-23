"""
The answer hides behind the academic sounding term structural
 subtyping. One way to categorize type systems is by whether 
 they are nominal or structural:

In a nominal system, comparisons between types are based on 
names and declarations. The Python type system is mostly nominal,
 where an int can be used in place of a float because of their 
 subtype relationship.

In a structural system, comparisons between types are based on 
structure. You could define a structural type Sized that includes
 all instances that define .__len__(), irrespective of their
  nominal type.
"""


from typing import Sized


# A protocol specifies one or more methods that must be implemented. 
# For example, all classes defining .__len__() fulfill the typing.Sized protocol.
#  We can therefore annotate len() as follows:

def len(obj: Sized) -> int:
    return obj.__len__()



from typing_extensions import Protocol

class Sized(Protocol):
    def __len__(self) -> int: ...

    def len(obj: Sized) -> int:
        return obj.__len__()

