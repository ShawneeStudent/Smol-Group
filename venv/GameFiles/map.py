import xml.etree.ElementTree as ET
import re


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
        self.parseXMl(mapName)

    def parseXMl(self, fileName):
        try:
            mapXML = ET.parse("TMXFiles\\" + fileName)
            root = mapXML.getroot()
            self.mTileWidth = root.attrib["tilewidth"]
            self.mTileHeight = root.attrib["tileheight"]
            self.mMapWidth = root.attrib["width"]
            self.mMapHeight = root.attrib["height"]
            self.mNumTileColumns = 0
            tilecount = 0
            tilesetName = ""
            # find layers
            for child in root:  # <item> under map_obj
                if child.tag == "tileset":
                    self.mNumTileColumns = int(child.attrib["columns"])
                    tilecount = child.attrib["tilecount"]
                    self.mTileOffsetX = child.attrib["spacing"]
                    self.mTileOffsetY = child.attrib["spacing"]
                    tilesetName = child[0].attrib["source"]
                    print(tilesetName)

                else:  # if not <tileset> then we are <layer>
                    self.mTileCodes.append(["layer_num", child.attrib["id"]])
                    idx = 0
                    tmp_array = []
                    columns = int(child.attrib["width"])
                    for grandchild in child:  # tile number and render order
                        tiledata = grandchild.text
                        tiledata = tiledata.split(",")
                        tmp_arr = []
                        for sub in tiledata:  # doing black magic to remove newline characters
                            tmp_arr.append(re.sub('\n', '', sub))
                        tiledata = tmp_arr
                        for tilenum in tiledata:  # store each row in a tmp list then append to mTileCodes
                            tmp_array.append(tilenum)
                            if idx % columns == 0 and idx != 0:  # if idx is divided equally by columns and idx != 0
                                self.mTileCodes.append(tmp_array)
                                tmp_array = []
                            idx += 1
            print(self.mTileCodes)

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
#   the index of each tile number will also inform us where its at on the world map_obj
#
