class Candidate:
    def __init__(self, candidateID, candidateName, candidateAge, gender):
        self.candidateID = candidateID
        self.candidateName = candidateName
        self.candidateAge = candidateAge
        self.gender = gender

    def view_candidate_details(candidate):
        print("Candidate Details:")
        print(f"ID       : {candidate.candidateID}")
        print(f"Name     : {candidate.candidateName}")
        print(f"Age      : {candidate.candidateAge}")
        print(f"Gender   : {candidate.gender}")


