namespace SpriteKind {
    export const map2 = SpriteKind.create()
    export const rp = SpriteKind.create()
    export const bp = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile2`, function (sprite2, location2) {
    b = 0
})
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile2`, function (sprite, location) {
    r = 0
})
function newbuttons () {
    rx = randint(0, 44)
    ry = randint(0, 44)
    bx = randint(0, 44)
    by = randint(0, 44)
    r = 0
    b = 0
    while (bx == rx) {
        bx = randint(0, 44)
    }
    while (by == ry) {
        by = randint(0, 44)
    }
    tiles.setTileAt(tiles.getTileLocation(ry, rx), assets.tile`myTile`)
    tiles.setTileAt(tiles.getTileLocation(by, bx), assets.tile`myTile0`)
}
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile3`, function (sprite5, location5) {
    r = 0
})
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile6`, function (sprite3, location3) {
    b = 1
    tiles.setTileAt(location3, assets.tile`myTile6`)
})
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile5`, function (sprite6, location6) {
    r = 0
})
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile1`, function (sprite10, location10) {
    r = 1
    tiles.setTileAt(location10, assets.tile`myTile1`)
})
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile`, function (sprite4, location4) {
    r = 1
    tiles.setTileAt(location4, assets.tile`myTile1`)
})
info.onCountdownEnd(function () {
    game.setGameOverMessage(true, "BEEP!")
    game.gameOver(true)
})
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile0`, function (sprite11, location11) {
    b = 1
    tiles.setTileAt(location11, assets.tile`myTile6`)
})
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile3`, function (sprite8, location8) {
    b = 0
})
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile4`, function (sprite7, location7) {
    b = 0
})
scene.onOverlapTile(SpriteKind.bp, assets.tile`myTile5`, function (sprite9, location9) {
    b = 0
})
scene.onOverlapTile(SpriteKind.rp, assets.tile`myTile4`, function (sprite12, location12) {
    r = 0
})
let by = 0
let bx = 0
let ry = 0
let rx = 0
let r = 0
let b = 0
let x = 0
let y = 0
tiles.setCurrentTilemap(tilemap`level2`)
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), sprites.create(img`
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
    `, SpriteKind.rp))
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), sprites.create(img`
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
    `, SpriteKind.bp))
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.One))
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Two))
scene.cameraFollowSprite(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)))
scene.setBackgroundColor(5)
let list2 = [
assets.tile`myTile2`,
assets.tile`myTile3`,
assets.tile`myTile4`,
assets.tile`myTile5`
]
for (let index = 0; index < 45 * 45 + 44; index++) {
    tiles.setTileAt(tiles.getTileLocation(y, x), list2._pickRandom())
    y += 1
    if (y == 46) {
        y = 0
        x += 1
    }
}
newbuttons()
info.setScore(0)
info.startCountdown(301)
forever(function () {
    if (!(tiles.tileAtLocationEquals(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).tilemapLocation(), assets.tile`myTile`))) {
        tiles.setTileAt(tiles.getTileLocation(ry, rx), assets.tile`myTile`)
    }
})
forever(function () {
    if (!(tiles.tileAtLocationEquals(mp.getPlayerSprite(mp.playerSelector(mp.PlayerNumber.One)).tilemapLocation(), assets.tile`myTile0`))) {
        tiles.setTileAt(tiles.getTileLocation(by, bx), assets.tile`myTile0`)
    }
})
forever(function () {
    if (r == 1 && b == 1) {
        info.changeScoreBy(1)
        tiles.setTileAt(tiles.getTileLocation(by, bx), list2._pickRandom())
        tiles.setTileAt(tiles.getTileLocation(ry, rx), list2._pickRandom())
        newbuttons()
    }
})
