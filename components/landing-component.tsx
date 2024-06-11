'use Client'

import { Comfortaa } from "next/font/google";
import { cn } from "@/lib/utils";

const comfortaa = Comfortaa({
    weight:'700',
    subsets:['latin']
});

const LandingComponent = () => {
    return (
        <div className="px-10 pb-20">
            <h2 className="text-center text-4xl text-black font-extrabold mb-10">
                Our Project Properties
            </h2>
            <div className={cn('text-transparent  text-black', comfortaa.className)}>
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Eaque magnam facere voluptas ipsum perferendis ex officiis reprehenderit perspiciatis suscipit laudantium! Ab quam, qui ipsum eligendi laborum fugit porro nam ipsam accusantium accusamus beatae suscipit? Repellendus vel cum incidunt quo illum animi nesciunt illo ducimus reiciendis ea est consectetur vitae laboriosam optio aspernatur in consequuntur debitis provident quod, quibusdam, id perferendis! Aspernatur explicabo obcaecati perferendis.
            </div>
        </div>
    );
}
 
export default LandingComponent;