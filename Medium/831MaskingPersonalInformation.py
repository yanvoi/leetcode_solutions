class Solution:
    def maskPII(self, s: str) -> str:
        
        def masked_email():
            name, the_rest = s.split("@")
            domain, top_domain = the_rest.split(".")
            name, domain, top_domain = name.lower(), domain.lower(), top_domain.lower()

            return name[0] + "*" * 5 + name[-1] + "@" + domain + "." + top_domain

        def masked_phone_number():
            digits = "".join([char for char in s if char.isdigit()])
            country_code, local_number = digits[:-10], digits[-10:]

            if not country_code:
                return "***-***-" + local_number[-4:]
            elif len(country_code) == 1:
                return "+*-***-***-" + local_number[-4:]
            elif len(country_code) == 2:
                return "+**-***-***-" + local_number[-4:]
            else:
                return "+***-***-***-" + local_number[-4:]

        if "@" in s:
            return masked_email()
        return masked_phone_number()
