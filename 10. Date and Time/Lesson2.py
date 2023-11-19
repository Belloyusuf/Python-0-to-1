from datetime import timedelta

#  TODO TIME DELTA

"""
Only days, seconds and microseconds are stored internally. Arguments are converted to those units:
    # A millisecond is converted to 1000 microseconds.
    # A minute is converted to 60 seconds.
    # An hour is converted to 3600 seconds.
    # A week is converted to 7 days.


"""


delta = timedelta(
     days=50,
     seconds=37,
     microseconds=20,
     milliseconds=29000,
     minutes=20,
     hours=4,
     weeks=2
)

# Only days, seconds, and microseconds remain
print(delta)
