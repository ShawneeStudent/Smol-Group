import xml.etree.ElementTree as ET
import re
import math

class Map:
    """ Map Manager"""
    def __init__(self, mapName):
        #self.mTileImage # pygame surf that contains all of the tiles
        #self.mTileOffsetX
        #self.mTileOffsetY
        #self.mTileImageNumX
        #self.mTileImageNumY
        #self.mMapWidth # in tiles
        #self.mMapHeight
        self.mTileCodes = []

        self.parseXMl(mapName)


    def parseXMl(self, fileName):
        try:
            mapXML = ET.parse("TMXFiles\\"+fileName)
            root = mapXML.getroot()
            self.mTileWidth = int(root.attrib["tilewidth"])
            self.mTileHeight = int(root.attrib["tileheight"])
            self.mMapWidth = int(root.attrib["width"])
            self.mMapHeight = int(root.attrib["height"])

            self.mNumTileColumns = 0
            tilecount = 0
            tilesetName = ""
            # find layers
            for child in root:  # <item> under map
                if child.tag == "tileset":
                    self.mNumTileColumns = int(child.attrib["columns"])
                    tilecount = int(child.attrib["tilecount"])
                    self.mTileOffsetX = int(child.attrib["spacing"])
                    self.mTileOffsetY = int(child.attrib["spacing"])
                    tilesetName = child[0].attrib["source"]
                    self.mTilecount = int(child.attrib["tilecount"])
                    #print(tilesetName)

                else: # if not <tileset> then we are <layer>
                    self.mTileCodes.append(["layer_num", child.attrib["id"]])
                    idx = 0
                    tmp_array = []
                    columns = int(self.mMapWidth)
                    for grandchild in child:  # tile number and render order
                        tiledata = grandchild.text
                        tiledata = tiledata.split(",")
                        tmp_arr = []
                        for sub in tiledata: # doing black magic to remove newline characters
                            tmp_arr.append(re.sub('\n','',sub))
                        tiledata = tmp_arr
                        for tilenum in tiledata: # store each row in a tmp list then append to mTileCodes
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
        winWidthInTiles = math.floor(win_width / self.mTileWidth)
        winHeightInTiles = math.floor(win_height / self.mTileHeight)
        layerNumber = 0
        cameraTileX = math.floor(cameraWorldPos[0] / self.mTileWidth)   # these twos vars are the xy worldspace
        cameraTileY = math.floor(cameraWorldPos[1] / self.mTileHeight)  # coords of the tile at 0,0 screenspace
        for i in range(winHeightInTiles):
            #if i == 0 or i % self.mTilecount == 0:
            #    layerNumber = int(self.mTileCodes[i][1])
                #print(layerNumber)
            #else:
            #   self.mTileCodes[layerNumber]
            for j in range(winWidthInTiles):
                # find tile pos in world space
                # convert world space to screen space
                # blit to screen
                pass

        pass


#   left to right first then go down one row until complete
#   ------------------->
#   0 0 0 0 0 0 1 4 2 5  |
#   2 7 6 3 5 8 2 2 4 4  |
#   4 5 8 6 3 10 4 1 5 7 |
#   0 0 0 0 0 0 0 0 4 2  |
#   1 5 8 6 2 4 5 8 6 4  |
#   2 7 8 9 5 4 2 6 3 7  v
#
#   the index of each tile number will also inform us where its at on the world map
#