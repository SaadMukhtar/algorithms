from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = list(votes[0])
        voteMap = {
            k: [0 for i in range(len(teams)) ] for k in teams
        }
        for v in votes:
            for i in range(len(teams)):
                teamVote = v[i]
                voteMap[teamVote][i] += 1
    
        voted_names = sorted(voteMap.keys())
        return "".join(sorted(voted_names, key=lambda x: voteMap[x], reverse=True))
