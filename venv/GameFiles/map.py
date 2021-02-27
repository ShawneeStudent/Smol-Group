import xml.etree.ElementTree as ET
import re
import math
import pygame
class Map:
    """ Map Manager"""

    def __init__(self, mapName):
        # self.mTileImage # pygame surf that contains all of the tiles
        # self.mTileOffsetX
        # self.mTileOffsetY
        # self.mTileImageNumX
        # self.mTileImageNumY
        # self.mMapWidth # in tiles
        # self.mMapHeight
        self.mTileCodes = []
        self.mTilesheet = pygame.image.load("TMXFiles\\spritesheet_tiles.png")
        self.mLayerNum = 0

        self.parseXMl(mapName)

    def parseXMl(self, fileName):
        try:
            mapXML = ET.parse("TMXFiles\\" + fileName)
            root = mapXML.getroot()
            self.mTileWidth = int(root.attrib["tilewidth"])
            self.mTileHeight = int(root.attrib["tileheight"])
            self.mMapWidth = int(root.attrib["width"])
            self.mMapHeight = int(root.attrib["height"])

            self.mNumTileColumns = 0
            tilecount = 0
            tilesetName = ""
            # find layers
            for child in root:  # <item> under map_obj
                if child.tag == "tileset":
                    self.mNumTileColumns = 26 #had to set this by hand because the tmx is wrong
                    tilecount = int(child.attrib["tilecount"])
                    #self.mTileOffsetX = int(child.attrib["spacing"])
                    #self.mTileOffsetY = int(child.attrib["spacing"])
                    tilesetName = child[0].attrib["source"]
                    self.mTilecount = int(child.attrib["tilecount"])
                    #print(tilesetName)

                else:  # if not <tileset> then we are <layer>
                    self.mLayerNum += 1
                    self.mTileCodes.append([child.attrib["name"]])
                    idx = 0
                    tmp_array = []
                    columns = self.mMapWidth
                    for grandchild in child:  # tile number and render order
                        tiledata = grandchild.text
                        #print(tiledata)
                        tiledata = tiledata.split(",")
                        tmp_arr = []
                        for sub in tiledata:  # doing black magic to remove newline characters
                            tmp_arr.append(re.sub('\n', '', sub))
                        tiledata = tmp_arr
                        for tilenum in tiledata:  # store each row in a tmp list then append to mTileCodes
                            tmp_array.append(tilenum)
                            #if idx % columns == 0 and idx != 0: # if idx is divided equally by columns and idx != 0
                            #    self.mTileCodes.append(tmp_array)
                            #    tmp_array = []
                            #idx += 1
                        self.mTileCodes.append(tmp_array)
                        tmp_array = []
            #print(self.mTileCodes)
        except FileNotFoundError:
            print("Couldnt open file '", fileName, "'", sep="")



    def render(self, surf, cameraWorldPos, win_width, win_height):
        #(128, 160) or 8x10 in tiles or 18 tileIDX
        winWidthInTiles = math.floor(win_width / self.mTileWidth)
        winHeightInTiles = math.floor(win_height / self.mTileHeight)

        cameraTileX = math.floor(cameraWorldPos[0] / self.mTileWidth)
        cameraTileY = math.floor(cameraWorldPos[1] / self.mTileHeight)
        #print(cameraTileY)

        startTileIDX = cameraTileX+cameraTileY


        #print(startTileIDX)
        for k in range(self.mLayerNum):
            MoveDown = 0
            for i in range(winHeightInTiles):
                for j in range(winWidthInTiles):
                    #camera coords - tile coords = screen space coords for tiles
                    #tmpx = cameraWorldPos[0] - cameraTileX + (j * self.mTileWidth)
                    #tmpy = cameraWorldPos[1] - cameraTileY + (i * self.mTileHeight)
                    #print(tmpx,",", tmpy)
                    # blit to screen

                    #self.mMapWidth * k gets us to the correct layer idx 0
                    if k % 2 != 0: # since tilesheet goes [[layer name],[data]....] we do this to make sure we hit the data
                        CurrentTile = int(self.mTileCodes[k][startTileIDX + j + MoveDown]) # this is correct
                        print("[][thisone] = " , str(startTileIDX+ j + MoveDown), " tilecode= " , int(self.mTileCodes[k][startTileIDX + j + MoveDown]))
                        currentTileWorldSpaceX = cameraTileX + (j*self.mTileWidth)
                        currentTileWorldSpaceY = cameraTileY + (i*self.mTileHeight)

                        # ---------> CODE FOR FINDING CURRENT TILE POSITION IN THE TILESHEET
                        TilesheetY = int(CurrentTile/26)
                        TilesheetX = int((CurrentTile/26 - int(CurrentTile/26)) * 26)
                        #print(TilesheetX, ",",TilesheetY)
                        TilesheetY_InPixels = TilesheetY*self.mTileHeight
                        TilesheetX_InPixels = TilesheetX*self.mTileWidth
                        #print(TilesheetX_InPixels,",",TilesheetY_InPixels)
                        #<---------- END OF BLOCK


                        #print(tmpx," ",tmpy," ",tmp_tilesheetcoord, " ", self.mTileWidth)
                        surf.blit(self.mTilesheet, (j * self.mTileWidth, i * self.mTileHeight),
                                  ((TilesheetX_InPixels,
                                    TilesheetY_InPixels),
                                    (self.mTileWidth, self.mTileHeight)))
                MoveDown += self.mMapWidth


    def getMapSize(self):
        return (self.mMapWidth * self.mTileWidth, self.mMapHeight * self.mTileHeight)
#   left to right first then go down one row until complete
#   ------------------->
#   0 0 0 0 0 0 1 4 2 5  |
#   2 7 6 3 5 8 2 2 4 4  |
#   4 5 8 6 3 10 4 1 5 7 |
#   0 0 0 0 0 0 0 0 4 2  |
#   1 5 8 6 2 4 5 8 6 4  |
#   2 7 8 9 5 4 2 6 3 7  v
#
#   the index of each tile number will also inform us where its at on the world map_obj
#
