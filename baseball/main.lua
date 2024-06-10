
require 'src/Dependencies'

function love.load()
    love.graphics.setDefaultFilter('nearest', 'nearest')
    love.window.setTitle('Baseball')

    love.window.setMode(WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen=false,
        resizable=false, 
        vsync = true
    })

    gStateMachine = StateMachine {
        ['start'] = function() return StartState() end
    }
    gStateMachine:change('start')
end

function love.update(dt)
    gStateMachine:update(dt)

end

function love.draw()
    love.graphics.printf('Select Difficulty', 0, WINDOW_HEIGHT/8,WINDOW_WIDTH,'center')

end