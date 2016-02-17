import gzip
fp = gzip.open('/app/work/tasks/ThinkStats/2002FemResp.dat.gz')
counter = 0;
for i, line in enumerate(fp):
#     if i == None:
#         break
    counter = counter + 1

fp.close()

print 'the counter ', counter
