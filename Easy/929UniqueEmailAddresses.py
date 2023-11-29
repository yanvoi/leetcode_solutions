class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name, *_ = local_name.split("+")
            unique.add(local_name.replace(".", "") + "@" + domain_name)

        return len(unique)
