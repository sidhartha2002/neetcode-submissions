class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # approach :
        # 1. split the strings to local + domain part
        # 2. check if local string conatins any '+' then consider the first part before '+' as per the '+' rule
        # 3. check '.' present in the new local then replace it witn ""
        # 4. add this new fresh filtered local string to the set.
        # 5. Recombine the local + @ + domain to form unique email.
        # 6. return the len of the set


        unique_emails = set()

        for email in emails:
            # 1.
            local, domain = email.split('@')

            # 2.
            if "+" in local:
                local = local.split("+")[0] # split and consider only the first past before "+"
            # 3.
            local = local.replace(".", "")

            unique_emails.add(local + "@" + domain)

        return len(unique_emails)








            
