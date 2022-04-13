def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    return floodFillRecursion(image, sr,sc,newColor, image[sr][sc])
    
def floodFillRecursion(image, sr,sc, newColor, color):
    if sr < 0 or sr > len(image) - 1 or sc < 0 or sc>len(image[0]) - 1:
        return
    
    if image[sr][sc] == color:
        image[sr][sc] = newColor
        floodFillRecursion(image, sr-1, sc, newColor, color)
        floodFillRecursion(image, sr+1, sc, newColor, color)
        floodFillRecursion(image, sr, sc-1, newColor, color)
        floodFillRecursion(image, sr, sc+1, newColor, color)
    
    return image

print(floodFill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1,sc=1,newColor=2))