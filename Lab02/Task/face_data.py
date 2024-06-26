import numpy as np

Face1 = np.array([[-64.0, 39.0], [-63.0, 21.0], [-60.0, 3.0], [-57.0, -14.0], [-51.0, -31.0],
                  [-42.0, -47.0], [-30.0, -60.0], [-16.0, -70.0], [-1.0, -73.0], [15.0, -71.0],
                  [29.0, -60.0], [42.0, -48.0], [52.0, -32.0], [58.0, -16.0], [62.0, 2.0],
                  [64.0, 20.0], [64.0, 38.0], [-53.0, 47.0], [-45.0, 57.0], [-33.0, 60.0],
                  [-19.0, 60.0], [-7.0, 56.0], [8.0, 57.0], [20.0, 60.0], [33.0, 61.0],
                  [46.0, 56.0], [53.0, 47.0], [1.0, 42.0], [1.0, 28.0], [1.0, 14.0], [2.0, 0.0],
                  [-14.0, -7.0], [-7.0, -10.0], [1.0, -12.0], [9.0, -10.0], [16.0, -7.0],
                  [-39.0, 38.0], [-32.0, 41.0], [-24.0, 42.0], [-17.0, 37.0], [-24.0, 36.0],
                  [-32.0, 36.0], [17.0, 37.0], [24.0, 42.0], [32.0, 41.0], [40.0, 38.0],
                  [33.0, 35.0], [24.0, 35.0], [-25.0, -31.0], [-15.0, -28.0], [-6.0, -26.0],
                  [-0.0, -28.0], [7.0, -26.0], [15.0, -28.0], [25.0, -30.0], [16.0, -38.0],
                  [7.0, -42.0], [-0.0, -43.0], [-7.0, -43.0], [-16.0, -39.0], [-20.0, -32.0],
                  [-6.0, -32.0], [-0.0, -33.0], [7.0, -32.0], [20.0, -31.0], [7.0, -34.0],
                  [1.0, -35.0], [-6.0, -34.0]])
print(Face1.shape)
Face2 = np.array([[-64.0, 41.0], [-64.0, 23.0], [-62.0, 5.0], [-60.0, -13.0], [-53.0, -31.0],
                  [-43.0, -48.0], [-31.0, -62.0], [-17.0, -74.0], [-1.0, -77.0], [16.0, -74.0],
                  [30.0, -62.0], [42.0, -47.0], [53.0, -31.0], [59.0, -14.0], [63.0, 4.0],
                  [64.0, 21.0], [65.0, 39.0], [-53.0, 46.0], [-46.0, 55.0], [-34.0, 59.0],
                  [-21.0, 59.0], [-9.0, 55.0], [9.0, 55.0], [21.0, 58.0], [34.0, 58.0],
                  [46.0, 53.0], [53.0, 43.0], [1.0, 40.0], [1.0, 25.0], [1.0, 11.0],
                  [1.0, -3.0], [-18.0, -5.0], [-9.0, -9.0], [0.0, -13.0], [10.0, -9.0],
                  [18.0, -5.0], [-40.0, 36.0], [-32.0, 38.0], [-25.0, 38.0], [-18.0, 36.0],
                  [-25.0, 35.0], [-33.0, 35.0], [18.0, 35.0], [26.0, 37.0], [33.0, 36.0],
                  [41.0, 34.0], [33.0, 33.0], [26.0, 34.0], [-35.0, -20.0], [-23.0, -20.0],
                  [-11.0, -20.0], [-1.0, -22.0], [9.0, -21.0], [20.0, -20.0], [32.0, -20.0],
                  [21.0, -38.0], [9.0, -46.0], [-1.0, -48.0], [-12.0, -46.0], [-25.0, -38.0],
                  [-31.0, -22.0], [-11.0, -24.0], [-1.0, -26.0], [9.0, -24.0], [28.0, -22.0],
                  [9.0, -37.0], [-1.0, -39.0], [-11.0, -38.0]])

Face3 = np.array([[-66.0, 36.0], [-65.0, 17.0], [-63.0, -1.0], [-59.0, -19.0], [-52.0, -37.0],
                  [-44.0, -54.0], [-33.0, -68.0], [-19.0, -78.0], [-3.0, -81.0], [13.0, -78.0],
                  [27.0, -68.0], [40.0, -56.0], [50.0, -40.0], [57.0, -23.0], [62.0, -5.0],
                  [64.0, 13.0], [65.0, 32.0], [-51.0, 58.0], [-44.0, 69.0], [-32.0, 73.0],
                  [-19.0, 73.0], [-8.0, 68.0], [12.0, 68.0], [23.0, 73.0], [36.0, 74.0],
                  [47.0, 69.0], [54.0, 58.0], [2.0, 47.0], [2.0, 34.0], [2.0, 23.0],
                  [2.0, 10.0], [-13.0, -2.0], [-6.0, -4.0], [1.0, -6.0], [7.0, -5.0],
                  [14.0, -2.0], [-39.0, 41.0], [-32.0, 46.0], [-23.0, 46.0], [-16.0, 41.0],
                  [-24.0, 39.0], [-32.0, 38.0], [18.0, 40.0], [25.0, 46.0], [34.0, 45.0],
                  [41.0, 40.0], [34.0, 37.0], [25.0, 38.0], [-20.0, -36.0], [-14.0, -27.0],
                  [-6.0, -22.0], [-1.0, -24.0], [5.0, -22.0], [12.0, -28.0], [18.0, -38.0],
                  [12.0, -48.0], [4.0, -53.0], [-2.0, -54.0], [-8.0, -53.0], [-15.0, -47.0],
                  [-16.0, -36.0], [-6.0, -29.0], [-1.0, -29.0], [4.0, -29.0], [14.0, -37.0],
                  [4.0, -43.0], [-1.0, -44.0], [-7.0, -43.0]])



TargetFace1 = np.array([[-65.2, 37.6], [-64.4, 19.0], [-62.2, 1.0], [-58.8, -16.8], [-52.0, -34.6], [-43.4, -51.4], [-32.0, -65.2], [-18.0, -75.6], [-2.2, -78.6], [14.0, -75.8], [28.0, -65.2], [40.8, -52.6], [51.0, -36.6], [57.6, -19.8], [62.2, -1.8], [64.0, 16.0], [64.8, 34.6], [-51.8, 53.4], [-44.6, 63.8], [-32.6, 67.6], [-19.4, 67.6], [-8.0, 63.0], [10.6, 63.2], [22.0, 67.4], [35.0, 68.2], [46.6, 63.2], [53.6, 52.8], [1.6, 44.6], [1.6, 31.0], [1.6, 18.8], [1.8, 5.4], [-14.2, -3.6], [-6.8, -6.2], [0.8, -8.6], [8.0, -6.8], [15.2, -3.6], [-39.2, 39.4], [-32.0, 43.4], [-23.6, 43.6], [-16.6, 39.2], [-24.2, 37.6], [-32.2, 37.0], [17.8, 38.4], [25.0, 43.4], [33.4, 42.4], [40.8, 38.4], [33.6, 35.8], [25.0, 36.6], [-24.0, -31.8], [-16.0, -25.8], [-7.0, -22.4], [-0.8, -24.4], [6.2, -22.6], [14.2, -26.4], [22.2, -32.8], [14.6, -44.0], [5.6, -49.4], [-1.4, -50.6], [-8.6, -49.6], [-17.2, -43.6], [-19.8, -32.4], [-7.0, -28.6], [-0.8, -29.2], [5.6, -28.6], [18.0, -32.8], [5.6, -40.0], [-0.6, -41.2], [-7.6, -40.2]])

TargetFace2 = np.array([[-77.6, 46.6], [-76.9, 24.6], [-74.2, 3.0], [-70.7, -18.3], [-62.6, -39.6], [-51.7, -59.7], [-37.7, -76.2], [-20.9, -89.2], [-2.0, -92.8], [17.7, -89.5], [34.5, -76.2], [49.6, -60.3], [62.1, -41.1], [69.7, -21.0], [74.9, 0.6], [76.8, 21.7], [77.7, 43.7], [-62.8, 60.3], [-54.1, 72.2], [-39.7, 76.7], [-23.8, 76.7], [-9.8, 71.5], [11.7, 71.8], [25.7, 76.2], [41.3, 76.9], [55.6, 70.9], [64.0, 58.8], [1.6, 51.4], [1.6, 34.5], [1.6, 18.9], [1.9, 2.5], [-18.4, -5.4], [-9.0, -9.1], [0.7, -12.5], [10.5, -9.5], [19.4, -5.4], [-47.3, 45.8], [-38.4, 49.7], [-28.9, 50.0], [-20.5, 45.5], [-29.3, 43.9], [-38.9, 43.5], [21.3, 44.6], [30.2, 49.5], [39.7, 48.3], [48.9, 44.4], [40.0, 41.8], [30.2, 42.7], [-33.0, -33.7], [-21.6, -29.2], [-9.7, -26.6], [-0.9, -29.0], [8.6, -27.1], [19.3, -29.6], [30.7, -34.2], [20.1, -49.6], [8.2, -56.8], [-1.3, -58.5], [-11.3, -57.1], [-23.3, -49.5], [-27.9, -35.0], [-9.7, -33.2], [-0.9, -34.5], [8.2, -33.2], [25.6, -35.1], [8.2, -45.9], [-0.6, -47.6], [-10.1, -46.4]])



edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
         (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16),
         (17, 18), (18, 19), (19, 20), (20, 21),
         (22, 23), (23, 24), (24, 25), (25, 26),
         (27, 28), (28, 29), (29, 30), (30, 33), (31, 32), (32, 33), (33, 34), (34, 35),
         (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 36),
         (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 42),
         (48, 49), (49, 50), (50, 51), (51, 52), (52, 53), (53, 54),
         (54, 55), (55, 56), (56, 57), (57, 58), (58, 59), (59, 48),
         (60, 61), (61, 62), (62, 63), (63, 64), (64, 65), (65, 66), (66, 67), (67,60)]