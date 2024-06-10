StartState = Class{__includes = BaseState}

local highlighted = 1

function StartState:update(dt)
    if love.keyboard.wasPressed('up') then
        highlighted = 2
    end
end

function StartState:render()
    love.graphics.setColor(1,1,1,1)
end