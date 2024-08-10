@namespace
class SpriteKind:
    map2 = SpriteKind.create()
    rp = SpriteKind.create()
    bp = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global r
    r = 0
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    global b
    b = 0
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile2
    """),
    on_overlap_tile2)

def newbuttons():
    global rx, ry, bx, by, r, b
    rx = randint(0, 44)
    ry = randint(0, 44)
    bx = randint(0, 44)
    by = randint(0, 44)
    r = 0
    b = 0
    while bx == rx:
        bx = randint(0, 44)
    while by == ry:
        by = randint(0, 44)
    tiles.set_tile_at(tiles.get_tile_location(ry, rx),
        assets.tile("""
            myTile
        """))
    tiles.set_tile_at(tiles.get_tile_location(by, bx),
        assets.tile("""
            myTile0
        """))

def on_countdown_end():
    game.set_game_over_message(True, "BEEP!")
    game.game_over(True)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile3(sprite3, location3):
    global b
    b = 1
    tiles.set_tile_at(location3, assets.tile("""
        myTile6
    """))
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile6
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    global r
    r = 1
    tiles.set_tile_at(location4, assets.tile("""
        myTile1
    """))
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    global r
    r = 0
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    global r
    r = 0
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    global b
    b = 0
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite8, location8):
    global b
    b = 0
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile3
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite9, location9):
    global b
    b = 0
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite10, location10):
    global r
    r = 1
    tiles.set_tile_at(location10, assets.tile("""
        myTile1
    """))
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite11, location11):
    global b
    b = 1
    tiles.set_tile_at(location11, assets.tile("""
        myTile6
    """))
scene.on_overlap_tile(SpriteKind.bp,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite12, location12):
    global r
    r = 0
scene.on_overlap_tile(SpriteKind.rp,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile12)

by = 0
bx = 0
ry = 0
rx = 0
b = 0
r = 0
tiles.set_current_tilemap(tilemap("""
    level2
"""))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 2 2 f f f . . . . 
                . . . f f f 2 2 2 2 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 2 2 2 2 2 2 e e f . . 
                . . f e 2 f f f f f f 2 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        SpriteKind.rp))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
    sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                . . . . f f f 8 8 f f f . . . . 
                . . . f f f 8 8 8 8 f f f . . . 
                . . f f f e e e e e e f f f . . 
                . . f f e 8 8 8 8 8 8 e e f . . 
                . . f e 8 f f f f f f 8 e f . . 
                . . f f f f e e e e f f f f . . 
                . f f e f b f 4 4 f b f e f f . 
                . f e e 4 1 f d d f 1 4 e e f . 
                . . f e e d d d d d d e e f . . 
                . . . f e e 4 4 4 4 e e f . . . 
                . . e 4 f 8 8 8 8 8 8 f 4 e . . 
                . . 4 d f 8 8 8 8 8 8 f d 4 . . 
                . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                . . . . . f f f f f f . . . . . 
                . . . . . f f . . f f . . . . .
        """),
        SpriteKind.bp))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO))
scene.camera_follow_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))
scene.set_background_color(5)
list2 = [assets.tile("""
        myTile2
    """),
    assets.tile("""
        myTile3
    """),
    assets.tile("""
        myTile4
    """),
    assets.tile("""
        myTile5
    """)]
x = 0
y = 0
for index in range(45 * 45 + 44):
    tiles.set_tile_at(tiles.get_tile_location(y, x), list2._pick_random())
    y += 1
    if y == 46:
        y = 0
        x += 1
newbuttons()
info.set_score(0)
info.start_countdown(301)

def on_forever():
    if not (tiles.tile_at_location_equals(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).tilemap_location(),
        assets.tile("""
            myTile
        """))):
        tiles.set_tile_at(tiles.get_tile_location(ry, rx),
            assets.tile("""
                myTile
            """))
forever(on_forever)

def on_forever2():
    if not (tiles.tile_at_location_equals(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).tilemap_location(),
        assets.tile("""
            myTile0
        """))):
        tiles.set_tile_at(tiles.get_tile_location(by, bx),
            assets.tile("""
                myTile0
            """))
forever(on_forever2)

def on_forever3():
    if r == 1 and b == 1:
        info.change_score_by(1)
        tiles.set_tile_at(tiles.get_tile_location(by, bx), list2._pick_random())
        tiles.set_tile_at(tiles.get_tile_location(ry, rx), list2._pick_random())
        newbuttons()
forever(on_forever3)
