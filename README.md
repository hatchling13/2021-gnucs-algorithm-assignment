# 개요
이 저장소는 2021년 2학기 경상대학교 컴퓨터과학과에서 진행된 알고리즘 강의의 과제 중 하나였던 `최소 신장 트리 그리기` 관련 자료를 정리 및 보관하기 위한 저장소이다.
# 요약
본 프로그램은 가중치가 주어진 간선과 정점으로 만들 수 있는 최소 신장 트리(Minimum Spanning Tree)를 구하여, 그 결과를 도식화한 것을 보여주는 것이 주 목표이다. README에서는 크게 3가지의 문제 요소를 간단히 기술한다.
## 문제
- 무향 그래프이므로, 같은 정점 두 개를 시작과 끝으로 하는 간선은 한 개 이상 존재하지 않아야 한다.
- 루프가 존재하지 않아야 한다.
- 간선이 정점과 겹치는 부분이 존재하지 않아야 한다.
## 해결법
- 정점의 수가 적으므로, 중복 판정을 진행할 간선의 시작/종료 정점을 그래프 내의 모든 간선과 연결된 정점에 대해 비교하여 같은 것이 있다면 제외시킨다.
- 드롭다운 메뉴를 이용하여 정점을 선택하기 때문에, 이미 선택된 정점은 반대쪽 드롭다운 메뉴에서 삭제하여 고를 수 없게 한다.
- 사용중인 그래픽 모듈 `tkinter`는 `Canvas`에 그려진 객체에 대한 Bounding Box를 반환하는 함수를 제공한다. 이를 이용하여 1차적으로 충돌 판정을 진행한다. 이후, 원과 직선의 관계를 이용하여 판별식을 세운다. `(원의 방정식) = (직선의 판별식)` 꼴로 놓은 후 매개변수 t에 관한 방정식으로 바꾸고, t의 2차방정식 꼴로 정리하여 판별식 D를 유도하는 형식이다. 주어진 간선은 사실 직선이 아닌 선분이지만, Bounding Box를 이용한 1차 충돌 판정을 거쳤기 때문에 2차 판정 시 정점은 항상 간선 근처에 존재하게 된다.
# 결론
- 그래픽 관련 문제 해결에 수학적인 지식은 큰 도움이 된다는 것을 알 수 있었다.
- Prim 알고리즘과 Kruskal 알고리즘을 실습해볼 수 있는 좋은 기회가 되었다.