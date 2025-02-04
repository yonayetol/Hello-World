class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict = Counter()
        for sub in cpdomains:
            count,domain = sub.split(" ")
            count = int(count) 
            domain = domain.split(".")
            # domain will look like something like this =  [google, mail, com]

            for i_word in range(len(domain)):
                my_dict[".".join(domain[i_word:])] += count

        return [f"{str(count)} {dom}" for dom,count in my_dict.items()]
           


