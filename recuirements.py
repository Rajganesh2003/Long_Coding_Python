class Utils:
    @staticmethod
    def getMonth(month):
        months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]
        return (months.index(month)+1)
        
    @staticmethod    
    def getAggrigateMarks(marks):
        total=sum(marks)
        percentage=total/3
        return percentage

class RecruitingTeam:
    def __init__(self,candidate):
        self.candidate=candidate
        
    def checkDobOfCandidate(self):
        month=self.candidate.dob[0]
        year=int(self.candidate.dob[1])
        if(year>=1999 and Utils.getMonth(month)>=7):
            return True
        return False
            
    def checkAggrigateMarks(self):
        marks=self.candidate.aggregateMarks
        candidateCommunity=self.candidate.community
        aggregateMarks=Utils.getAggrigateMarks(marks)
        if(aggregateMarks>=60):
            return True
        elif(candidateCommunity.lower()=="SC" or candidateCommunity.lower()=="ST" and aggregateMarks>=50):
            return True
        return False
            
    def checkUgCgpa(self):
        cgpa=self.candidate.UgCgpa
        if(cgpa>=8):
            return True
        return False
        
    def checkPgCgpa(self):
        cgpa=self.candidate.PgCgpa
        if(cgpa>=8):
            return True
        return False  
        
    def checkProjectsCount(self):
        count=self.candidate.ProjectsCount
        if(count>=2):
            return True
        return False
        
    def checkModeOfStudy(self):
        modeOfStudy=self.candidate.ModeOfStudy
        if(modeOfStudy.lower()=="full-time"):
            return True
        return False
    
    def checkInterviewScore(self):
        score=self.candidate.interviewScore
        if(score>=35):
            return True
        return False
        
    def checkNationality(self):
        nationality=self.candidate.Nationality
        if(nationality.lower()=="indian"):
            return True
        return False
        
    def getResults(self):
        dob=self.checkDobOfCandidate()
        aggregateMarks=self.checkAggrigateMarks()
        ugCgpa=self.checkUgCgpa()
        pgCgpa=self.checkPgCgpa()
        projectsCount=self.checkProjectsCount()
        modeOfStudy=self.checkModeOfStudy()
        interviewScore=self.checkInterviewScore()
        nationality=self.checkNationality()
        if(dob and aggregateMarks and ugCgpa and pgCgpa and projectsCount and modeOfStudy and interviewScore and nationality):
            return True
        return False    

class HrTeam:
    def __init__(self,recruitingTeam,candidate):
        self.recruitingTeam=recruitingTeam
        self.candidate=candidate
    
    def getFinalResults(self):
        return self.recruitingTeam.getResults()
        
    def informFinalResults(self):
        result= self.getFinalResults()
        if(result):
            return print("The Candidate is Selected")
        return print("The Candidate is Not Selected ")    

class Candidate:
    def __init__(self,name,dob,community,aggregateMarks,UgCgpa,PgCgpa,ProjectsCount,ModeOfStudy,Nationality,interviewScore):
        self.name=name
        self.dob=dob
        self.community=community
        self.aggregateMarks=aggregateMarks
        self.UgCgpa=UgCgpa
        self.PgCgpa=PgCgpa
        self.ProjectsCount=ProjectsCount
        self.ModeOfStudy=ModeOfStudy
        self.Nationality=Nationality
        self.interviewScore=interviewScore

class AbcCompany:
    def __init__(self,candidate):
        self.candidate=candidate
        
    def interview(self):
        recruitingTeam=RecruitingTeam(candidate)
        hrteam=HrTeam(recruitingTeam,candidate)
        hrteam.informFinalResults()
        
        
def getCandidate():
    print("Enter Your Name : ")
    name=input().strip()
    print("Enter Your Dob: sample(July 1999) : ")
    dob=list(map(str,input().split()))
    print("Enter Your Community : ")
    community=input().strip()
    print("Enter Your Physics,Chemistry and Maths/Biology Marks : ")
    aggregateMarks=list(map(int,input().split()))
    print("Enter Your UG CGPA : ")
    UgCgpa=float(input())
    print("Enter Your PG CGPA : ")
    PgCgpa=float(input())
    print("Enter The No. Of Projects You Have done : ")
    ProjectsCount=int(input())
    print("Part-Time / Full-Time : ")
    ModeOfStudy=input().strip()
    print("Enter Your Nationality : ")
    Nationality=input().strip()
    print("Enter Your Interview Score : ")
    interviewScore=int(input())
    candidate=Candidate(name,dob,community,aggregateMarks,UgCgpa,PgCgpa,ProjectsCount,ModeOfStudy,Nationality,interviewScore)
    return candidate

if __name__ == "__main__":
    candidate=getCandidate()
    abcCompany=AbcCompany(candidate)
    abcCompany.interview()