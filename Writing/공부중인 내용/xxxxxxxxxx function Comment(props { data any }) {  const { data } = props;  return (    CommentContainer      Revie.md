```
function Comment(props: { data: any }) {
  const { data } = props;
  return (
    <CommentContainer>
      <ReviewProfile data={DummyData2} />
      <ProfileImg src={data.userImg} alt="이미지" />
      <StarRating rates={4.5} />
      <UserWrapper>
        <Username>{data.username}</Username>
        <UserId>{data.userId}</UserId>
        <AlignWrapper>
          <img src={Heart} alt="img" />
          <p>{data.like}</p>
        </AlignWrapper>
      </UserWrapper>
      <CommentWrapper>
        <FlexWrapper>
          <p>{data.score}</p>
          <p>별점</p>
          <p className="date">{data.date}</p>
        </FlexWrapper>
        <Flex>{StarRate()}</Flex>
        <CommentContent>{data.content}</CommentContent>
      </CommentWrapper>
    </CommentContainer>
  );
}
```





const Container = styled.div`

 display: flex;

 justify-content: center;

`;



![image-20230309131055605](C:\Users\sell\AppData\Roaming\Typora\typora-user-images\image-20230309131055605.png)



![image-20230309131110908](C:\Users\sell\AppData\Roaming\Typora\typora-user-images\image-20230309131110908.png)



![image-20230309131128949](C:\Users\sell\AppData\Roaming\Typora\typora-user-images\image-20230309131128949.png)



```
import styled from 'styled-components';
import { BookCarouselType } from 'Types/BookRankCarousel/type';
import { useRef, useState, useEffect } from 'react';
import BookRankCard from './BookRankCard';



export default function Carousel() {
  const [isMoved, setIsMoved] = useState(false);
  const translateX = (e: React.MouseEvent) => {
    if (isMoved && carouselRef && carouselRef.current) {
      carouselRef.current.scrollLeft += e.movementX;
    }
  };

  const carouselRef = useRef<HTMLDivElement>(null);

  return (
    <Container
      onMouseDown={() => setIsMoved(true)}
      onMouseUp={() => setIsMoved(false)}
      onMouseMove={(e) => translateX(e)}
      ref={carouselRef}
      className="carousel-body"
      draggable="false">
      {sortedDatas.map((book: BookCarouselType, idx: number) => (
        <Wrapper key={book.name}>
          <p className="carousel-body__title">{idx + 1}</p>
          <BookRankCard book={book} />
        </Wrapper>
      ))}
    </Container>
  );
}

const Container = styled.div`
  overflow-x: scroll;
  display: flex;
  box-sizing: border-box;
  margin-top: 1.3vh;
  -ms-overflow-style: none; /* Internet Explorer 10+ */
  scrollbar-width: none; /* Firefox */
  ::-webkit-scrollbar {
    display: none; /* Safari and Chrome */
  }
`;

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  margin-right: 1.46vw;
  align-items: center;
  justify-content: center;

  & > .carousel-body__title {
    font-style: italic;
    font-weight: 600;
    font-size: 1.85vh;
    line-height: 2.13vh;
    color: #969696;
    margin-bottom: 1.2vh;
  }
`;

```



![image-20230310163238871](C:\Users\sell\AppData\Roaming\Typora\typora-user-images\image-20230310163238871.png)

![image-20230310163247743](C:\Users\sell\AppData\Roaming\Typora\typora-user-images\image-20230310163247743.png)