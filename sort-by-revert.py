from __future__ import annotations
import random
from typing import Optional


class Reverter:
    """This class represents an array to be sorted. It formally encodes the states of the problem
    """
    
    def __init__(self,size:int,init=True) -> None:

        """The class only sorts an array containing numbers 1..size. The constructor shuffles the array
        in order to create an unsorted array.

        Args:
            size (int): the size of the array
            init (bool, optional): if True, the array is initialized with value 1..size, the shuffled, else, the array
            remains empty (it is used to clone the array). Defaults to True.
        """
        if init:
            self.table=list(range(1,size+1))
            random.shuffle(self.table)
            self.hash()
            self.parent=None
        else:
            self.table=[]
    
    
    def __str__(self) -> str:
        """returns a string representation of the object Reverter

        Returns:
            str: the string representation
        """
        return str(self.table)

    
    def hash(self):
        """Compute a hashcode of the array. Since it is not possible to hash a list, this one is first
        converted to a tuple
        """
        self.__hash__=hash(tuple(self.table))
    
    def __eq__(self, __value: Reverter) -> bool:
        """Tests whether the current object if equals to another object (Reverter). The comparison is made by comparing the hashcodes

        Args:
            __value (Reverter): _description_

        Returns:
            bool: True if self==__value, else it is False
        """
        return self.__hash__==__value.__hash__
    
    
    
    def is_the_goal(self) -> bool :
        """Tests whether the table is already sorted (so that the search is stopped)
        Returns:
            bool: True if the table is sorted, else it is False.
        """
        for i in range(1,len(self.table)):
            if self.table[i-1]>self.table[i]:return False
        return True

    def clone(self) -> Reverter:
        """This methods create a copy of the current object

        Returns:
            Reverter: the copy to be created
        """
        res=Reverter(len(self.table),False)
        res.table=[*self.table]
        res.parent=self
        return res
    
    def actions(self) -> list[Reverter]:
        """This class builds a list of possible actions. The returned list contains a set of tables depending of possible
        reverting of the current table

        Returns:
            list[Reverter]: the list of tables obtained after applying the possible reverting
        """
        res=[]
        sz=len(self.table)
        for i in range(sz):
            r=self.clone()
            v=self.table[i:]
            v.reverse()
            r.table=self.table[:i]+v
            r.hash()
            res.append(r)
        return res
        """largeur"""
    def solveBreadth(self) -> Optional[Reverter]:
            """This method implements breadth first search

            Returns:
                Optional[Reverter]: the sorted table is possible
                """

            open_set = [self]
            closed_set = []

            while open_set:
                current_node = open_set.pop(0)

                closed_set.append(current_node)


                if current_node.is_the_goal():
                    return current_node , open_set, closed_set

                successors = current_node.actions()

                for successor in successors:
                    if successor not in open_set and successor not in closed_set:
                        open_set.append(successor)
            return None


    """profendeur"""
    
    def solveDepth(self) -> Optional[Reverter]:
        """This method implements depth first search

        Returns:
            Optional[Reverter]: the sorted table if possible, None otherwise
        """
        # Mettre les nœuds de départ dans un ensemble OUVERT
        open_stack = [self]

        # Créer un ensemble vide FERME
        closed_set = []

        while open_stack:
            # Sélectionner le dernier nœud de OUVERT, soit le nœud n
            current_node = open_stack.pop()

            # L’enlever de OUVERT et le mettre dans FERME
            closed_set.append(current_node)

            # Si n est un nœud but, alors la recherche termine avec succès
            if current_node.is_the_goal():
                return current_node , open_stack , closed_set

            # Calculer les successeurs de n et les mettre dans l’ensemble M
            successors = current_node.actions()

            for successor in successors:
                # Les nœuds de M qui n’apparaissent ni dans OUVERT ni dans FERME
                # sont rajoutés à OUVERT
                if successor not in open_stack and successor not in closed_set:
                    open_stack.append(successor)

        # Si OUVERT est vide, alors échec de la recherche
        return None


    
    def solveRandom(self, max_iterations: int = 1000) -> Optional[Reverter]:
        """This method implements random search

        Args:
            max_iterations (int, optional): Maximum number of iterations before giving up. Defaults to 1000.

        Returns:
            Optional[Reverter]: the sorted table if possible
            """
    def solveHeuristic1(self) -> Optional[Reverter]:
        """This method implements heuristic search (heuristic n° 1:)
        Returns:
            Optional[Reverter]: the sorted table is possible
        """


    def solveHeuristic2(self) -> Optional[Reverter]:
        """This method implements heuristic search heuristic n°2

        Returns:
            Optional[Reverter]: the sorted table if possible
        """

    def solveHeuristic2(self) -> Optional[Reverter]:
        """This method implements heuristic search (heuristic n° 2)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """

    # Ajoute cette méthode à la classe Reverter
     #Reverter.solveHeuristic2 = solveHeuristic2

        #raise NotImplementedError("This method is not yet implemented")
    
    
    def solveHeuristic3(self) -> Optional[Reverter]:
        """This method implements heuristic search (your proposed heuristic)

        Returns:
            Optional[Reverter]: the sorted table is possible
        """

        #raise NotImplementedError("This method is not yet implemented")




size=8#,...,15,...
rev=Reverter(size,True)
print("Tableau init :", rev)

r1 = rev.solveBreadth()
r2 = rev.solveDepth()

print("{:<15} {:<25} {:<25} {:<25}".format("Method", "Sorted Table", "Open Set Size", "Closed Set Size"))
print("{:<15} {:<25} {:<25} {:<25}".format("Breadth First", str(r1[0]), len(r1[1]), len(r1[2])))
print("{:<15} {:<25} {:<25} {:<25}".format("Depth First", str(r2[0]), len(r2[1]), len(r2[2])))

"""size=5#8,...,15,...
rev=Reverter(size,True)
r1=rev.solveBreadth()
print(r1)"""
