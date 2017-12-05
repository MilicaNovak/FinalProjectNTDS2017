Milestones to be reached:

1. Dataset fixing: some lines are not well aligned so there is a shift in categories, this needs to be fixed
2. Convert 2 files of dataset into a useful form: use it to prepare a pandas Frame e. g. form needed for our overlap functions and data exploration, which is easy to handle. Current form, encapsulated JSON is quite unhelpful for us. Also, there is plenty of useless information in the original dataset (link to the actor photo, creditIDs,…) and  missing values need to be fixed.
  * Data visualization: visualize budget & revenue distributions, most frequently featuring actors, most common keywords, most frequent words in annotations,…
3. Prepare overlap functions and apply them on the categorical variables, e. g. get feature overlap matrices for each categorical variables – basically text overlap and comparing
4. Prepare similarity matrices using numerical features
5. Prepare function which combines matrices from 3 & 4  (in a way determined by input parameters of this function) and returns sparse weight matrix, Laplacian matrix, degree distribution [ exact details to be discussed ]
6. Function that visualize outputs of 5
7. … [to be discussed]