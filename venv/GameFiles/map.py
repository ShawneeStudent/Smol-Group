import xml.etree.ElementTree as ET

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
        #self.mTileCodes = []
        self.parseXMl(mapName)


    def parseXMl(self, fileName):
        try:
            print("TMXFile\\"+fileName)
            mapXML = ET.parse("TMXFile\\"+fileName)
            print("yeet")
            root = mapXML.getroot()
            self.mTileWidth = root.attrib("tilewidth")
            self.mTileHeight = root.attrib("tileheight")
            self.mMapWidth = root.attrib("width")
            self.mMapHeight = root.attrib("height")
            columns
            tilecount
            tilesetName
            # find layers
            for child in root:  # <item> under map
                if child.tag == "tileset":
                    columns = child.attrib("columns")
                    tilecount = child.attrib("tilecount")
                    self.mTileOffsetX = child.attrib("spacing")
                    self.mTileOffsetY = child.attrib("spacing")
                    tilesetName = child[0][1].attrib("source")

                else: # if not <tileset> then we are <layer>
                    self.mTileCodes.append(["layer_num", child.attrib("id")])
                    idx = 0
                    tmp_array = []
                    for grandchild in child:  # tile number and render order
                        tiledata = grandchild.text
                        tiledata.split(",")
                        for tilenum in tiledata: # store each row in a tmp list then append to mTileCodes
                            tmp_array.append(tilenum)
                            if idx % columns == 0: # columns - 1 if tiled is base 1 not base 0
                                self.mTileCodes.append(tmp_array)
                                tmp_array = []
                            idx += 1



        except FileNotFoundError:
            print("Couldnt open file '", fileName, "'", sep="")



    def render(self, surf):
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