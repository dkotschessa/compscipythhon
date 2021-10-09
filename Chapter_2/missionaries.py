from __future__ import annotations

from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries # west bank missionariees
        self.wc: int = cannibals # west bank cannibals
        self.em: int = MAX_NUM - self.wm # east bank missionaries
        self.ec: int = MAX_NUM - self.wc # east bank cannibals
        self.boat: bool = boat
        self.bank: str = "west" if self.boat else "east"

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True
    
    def goal_test(self) -> bool:
        legal = self.is_legal
        all_missionaries_east = self.em == MAX_NUM
        all_cannibals_east = self.ec == MAX_NUM
        return legal and all_cannibals_east  and all_missionaries_east
    
    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []

        if self.boat: # boat on west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc-2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc-1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm -1, self.wc -1, not self.boat))
        else: # boat on east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]
            

    def __str__(self):
        return ("On the west bank there are {} missionaries and {} cannibals.\n"
                "On the east bank there are {} missionaries and {} cannibals.\n"
                "The boat is on the {} bank.")\
            .format(self.wm, self.wc, self.em, self.ec, self.bank)


def display_solution(path: List[MCState]):
    if len(path) == 0: #sanity check
        return
    old_state = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank.\n".format(old_state.em - current_state.em, old_state.ec - current_state.ec))
        else:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank.\n".format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
        print(current_state)
        old_state = current_state

